[![Build Status](https://travis-ci.org/zaurilla/MathLib.svg?branch=master)](https://travis-ci.org/zaurilla/MathLib)

# MathLib

## Description

**MathLib** is my pet library for testing such instruments as **CMake**, **Conan**, **Catch2** and **Travis-CI**. All mathimatical functions are mirrored from `std`;

## How to build
```bash
mkdir build && cd build
conan install .. --build
cmake ..
cmake --build .
./bin/mathlib_tests
```
