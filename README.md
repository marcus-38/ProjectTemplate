# ProjectTemplate
My C++ Project Template

Based of TheCherno at https://github.com/TheCherno/ProjectTemplate/tree/master

Don't base your code on mine, I don't really know what I'm doing. Check out TheCherno instead.

## Prerequisite
This only works on Windows but should be easy to convert to Linux and MacOS. This will create a Visual Studio environment.

1. Install Conan from https://conan.io
2. Run
```
conan profile detect
```
3. Install Python from https://python.org
4. Install other requisites for your platform, i.e: cmake, build-essensial, xcode, visual studio ...

## What do I have to do to use this
To use this project template you have to check/edit the following:

1. Don't use this template, use https://github.com/TheCherno/ProjectTemplate/tree/master instead
2. make sure you have the correct architecture in premake5.lua
3. change project name, app name (if you want)
4. init.py will check which type of system you have and set accordingly
For Windows you can double click setup.bat instead
``` 
py.exe init.py
```

## TODO:
- [x] setup premake
- [x] switch to python script to setup everything
- [x] setup conan as package manager
- [x] let init.py switch on Visual Studio, Xcode, Makefile by os type
    - [x] check if it is working on Windows
    - [ ] check if it is working on MacOS
    - [x] check if it is working on Linux
- [ ] install python if missing
- [ ] install conan if missing
    - [ ] automatically run "conan profile detect --force"
- [ ] install other dependencies (cmake, build-essensial ...)
- [x] download premake5 is missing
    - [x] check if it is working on Windows
    - [ ] check if it is working on MacOS
    - [x] check if it is working on Linux