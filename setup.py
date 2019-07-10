import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="findmylibs",
    version="0.0.1",
    author="The Nomadic Coder",
    author_email="atemysemicolon@gmail.com",
    description="A package to probe installed libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atemysemicolon/findMyLibs",
    install_requires=['cmake'],
    packages=["findmylibs"],
    entry_points={
        'console_scripts': [
            'findmylibs = findmylibs.__main__:main',
            
        ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)