-- premake5.lua

include "../dependencies/conandeps.premake5.lua"

workspace "New Project"
    architecture "x64" -- change to your architecture
    configurations { "Debug", "Release" }
    startproject "App"
    location "../"

    -- workspace build options visual studio
    filter "system:windows"
        buildoptions { "/EHsc", "/Zc:preprocessor", "/Zc:__cplusplus" }
    
    project "App"
        kind "ConsoleApp"
        language "C++"
        cppdialect "C++20"
        targetdir "%{wks.location}/Build/%{cfg.buildcfg}/bin"
        objdir    "%{wks.location}/Build/%{cfg.buildcfg}/obj"
        staticruntime "off"

        location "../src"

        files 
        { 
            "%{prj.location}/**.h",
            "%{prj.location}/**.hpp",
            "%{prj.location}/**.c",
            "%{prj.location}/**.cpp"
        }

        filter "system:windows"
            systemversion "latest"
            defines { "WINDOWS" }

        filter "configurations:Debug"
            defines { "DEBUG" }
            runtime "Debug"
            symbols "On"

        filter "configurations:Release"
            defines { "RELEASE" }
            runtime "Release"
            optimize "On"
            symbols "Off"

        conan_setup()
        