project "Core"
    kind "StaticLib"
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
        "src"
    }

    targetdir ("../Binaries/" .. outputdir .. "/%{prj.name}")
    objdir ("../Binaries/Intermediates/" .. outputdir .. "/%{prj.name}")

    filter "system:windows"
        systemversion "latest"
        defines {}

    filter "configurations:Debug"
        defines { "DEBUG" }
        runtime "Debug"
        symbols "On"

    filter "configurations:Release"
        defines { "RELEASE" }
        runtime "Release"
        optimize "On"
        symbols "Off"