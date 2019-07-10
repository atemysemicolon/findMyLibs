# findMyLibs
Simple python application which interfaces with cmake and dumps libs


## Limitations 
- Only works for Linux with gcc
- Uses cmake, so cannot find what cmake cannot find
- Only finds cpp libraries usually, not libs built without cmake


## Usage
- Install : pip3 install -e git+https://github.com/atemysemicolon/findMyLibs
- Run : findmylibs <my-lib-name-to-search>