cmake_minimum_required(VERSION 3.0.0 FATAL_ERROR)
project(mathlib VERSION 0.1.0 LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(SRC_PATH ./src)
set(INCLUDE_PATH ./include)

set(SRC 
	${SRC_PATH}/mathlib/mathlib.cpp
	)

set(TEST_SRC 
	${SRC_PATH}/tests/test_main.cpp
	${SRC_PATH}/tests/test_functions.cpp
	)

# Library
add_library(${PROJECT_NAME} STATIC ${SRC})
target_include_directories(${PROJECT_NAME} PUBLIC ${INCLUDE_PATH})
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 17)

# Test
add_executable(${PROJECT_NAME}_tests ${TEST_SRC})
target_link_libraries(${PROJECT_NAME}_tests ${PROJECT_NAME} ${CONAN_LIBS})
set_property(TARGET ${PROJECT_NAME}_tests PROPERTY CXX_STANDARD 17)