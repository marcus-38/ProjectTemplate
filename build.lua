-- premake5.lua
workspace "New Project"
    architecture "x64" -- change to your architecture
    configurations { "Debug", "Release" }
    startproject "App"

    -- workspace build options visual studio
    filter "system:windows"
        buildoptions { "/EHsc", "/Zc:preprocessor", "/Zc:__cplusplus" }
    
    outputdir = "%{cfg.system}-%{cfg.architecture}/%{cfg.buildcfg}"

    group "Core"
        include "Core/Build-Core.lua"
    group ""

    include "External.lua"

    include "App/Build-App.lua"