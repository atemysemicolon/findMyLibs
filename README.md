# findMyLibs
Simple python application which interfaces with cmake and dumps libs

## Oops
Please note that despite I created this, there is an easier way on Linux to look for libs, with : `ldconfig -p | grep <my-lib-name>`
- Note to self : Always look at stackoverflow before solving a problem

## Limitations 
- Only works for Linux with gcc
- Uses cmake, so cannot find what cmake cannot find
- Only finds cpp libraries usually, not libs built without cmake


## Usage
- Install : `pip3 install -e git+https://github.com/atemysemicolon/findMyLibs`
- Run : `findmylibs <my-lib-name-to-search>`
