-- premake5.lua
workspace "New Project"
    architecture "ARM64"
    configurations { "Debug", "Release" }
    startproject "App"

    -- workspace build options visual studio
    filter "system:windows"
        buildoptions { "/EHsc", "/Zc:preprocessor", "/Zc:__cplusplus" }
    
    outputdir = "%{cfg.system}-%{cfg.architecture}/%{cfg.buildcfg}"

    group "Core"
        include "Core/Build-Core.lua"
    group ""

    include "App/Build-App.lua"