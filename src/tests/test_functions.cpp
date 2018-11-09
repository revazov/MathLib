#include "mathlib/mathlib.hpp"
#include "catch/catch.hpp"
#include <sstream>

TEST_CASE("Testing version output", "[streams]")
{
    std::ostringstream stream;
    print_version(stream);
    REQUIRE(stream.str() == "mathlib version: 0.1");
}
