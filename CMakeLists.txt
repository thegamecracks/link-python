cmake_minimum_required(VERSION 3.0)

project(LinkPython)

include(modules/link/AbletonLinkConfig.cmake)

add_subdirectory(modules/pybind11)

pybind11_add_module(_link src/Link.cpp)

target_link_libraries(_link PRIVATE Ableton::Link)
