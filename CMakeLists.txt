cmake_minimum_required(VERSION 3.0.0 FATAL_ERROR)
project(mathlib VERSION 0.1.0 LANGUAGES CXX)

set(SRC_PATH ./src)
set(INCLUDE_PATH ./include)
set(SRC ${SRC_PATH}/mathlib/mathlib.cpp)

add_library(${PROJECT_NAME} STATIC ${SRC})
target_include_directories(${PROJECT_NAME} PUBLIC ${INCLUDE_PATH})

set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 14)
# target_compile_options(${PROJECT_NAME} PUBLIC -std=c++17)

