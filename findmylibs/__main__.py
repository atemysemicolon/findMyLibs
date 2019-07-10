#!/usr/bin/env python3

import subprocess
from tempfile import mkdtemp
import os
import argparse

#  Necessary functions
def create_combinations(lib_query):
    return [lib_query, lib_query.capitalize(),
            lib_query.upper(), lib_query.lower()]


def look_for_pkg(query):
    proc = subprocess.Popen(["cmake", "--find-package",
                             "-DNAME={}".format(query),
                             "-DCOMPILER_ID=GNU", "-DLANGUAGE=C",
                             "-DMODE=EXIST"], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    output = proc.stdout.readlines()
    return not("not found" in str(output[0]))


def create_cmakelists(lib_name):
    print("-- Creating temporary cmake file")
    # Create sample cmake file
    cmake_lines = [
        "cmake_minimum_required(VERSION 3.13)\n"
        "project(query_find)\n",
        "find_package({})".format(lib_name)
    ]
    # Create a temporary folder
    my_tmp_folder = mkdtemp()
    cmake_file = os.path.join(my_tmp_folder, "CMakeLists.txt")
    with open(cmake_file, "w") as f:
        f.writelines(cmake_lines)
    return my_tmp_folder


def execute_cmake(cmake_folder):
    print("-- Execute cmake")
    proc = subprocess.Popen(["cmake", "."],
                            cwd=cmake_folder,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    error = proc.stderr.readlines()
    print(error)

    pass  # Pass Fail check needed here


def parse_cmake_cache(cmake_folder, lib_name):
    print("-- Parse CMakeCache.txt")
    cache_file = os.path.join(cmake_folder, "CMakeCache.txt")
    with open(cache_file, "r") as f:
        parsed_lines = f.readlines()
    for my_line in parsed_lines:
        if lib_name in my_line and "=" in my_line:
            print("\t--",my_line.split("\n")[0])


def main():
    # Parsed Args
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Display the library paths and executables "
                                        "of the given library name",
                        type=str)
    args = parser.parse_args()
    # Actual Process
    print("-- creating different combinations of the query. ")
    query_combinations = create_combinations(args.query)
    good_lib_name = None

    print("-- Looking for each query with cmake")
    for query in query_combinations:
        if look_for_pkg(query):
            good_lib_name = query
            break

    if good_lib_name:
        print(" \t-- Library found as : ", good_lib_name)
        cmake_tmp_folder = create_cmakelists(good_lib_name)
        execute_cmake(cmake_tmp_folder)
        parse_cmake_cache(cmake_tmp_folder, good_lib_name)
    else:
        print("Cmake cannot find any of the following : {}".
              format(query_combinations))


if __name__ == "__main__":
    main()




