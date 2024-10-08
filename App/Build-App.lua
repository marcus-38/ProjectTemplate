project "App"
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++20"
    targetdir "Binaries/%{cfg.buildcfg}"
    staticruntime "off"

    files 
    { 
        "src/**.h",
        "src/**.hpp",
        "src/**.c",
        "src/**.cpp"
    }

    includedirs
    {
        "src",
        -- include Core
        "../Core/src",
        "%{IncludeDirs.spdlog}"
    }

    links 
    {
        "Core"
    }

    targetdir ("../Binaries/" .. outputdir .. "/%{prj.name}")
    objdir ("../Binaries/Intermediates/" .. outputdir .. "%{prj.name}")

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