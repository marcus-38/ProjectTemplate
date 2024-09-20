#include "Core/Core.hpp"
#include "spdlog/spdlog.h"

int main() 
{
    spdlog::info("Including spdlog as logger");
    Core::PrintHelloWorld();
}