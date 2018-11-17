from conans import ConanFile, CMake

class MathlibConan(ConanFile):
    name = "MathLib"
    version = "4.0"
    license = "MIT"
    url = "https://github.com/zaurilla/MathLib"
    description = "MathLib is my pet library for testing c++ instruments"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "catch2/2.1.0@bincrafters/stable"
    exports_sources = [
        "include/*",
        "src/*",
        "CMakeLists.txt"
    ]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["mathlib"]

