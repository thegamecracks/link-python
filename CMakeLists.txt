cmake_minimum_required(VERSION 3.15...4.3)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

include(modules/link/AbletonLinkConfig.cmake)
pybind11_add_module(_link src/Link.cpp)
target_link_libraries(_link PRIVATE Ableton::Link)
install(TARGETS _link LIBRARY DESTINATION .)
