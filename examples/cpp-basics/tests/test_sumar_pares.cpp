#include "sumar_pares.hpp"

#include <cassert>
#include <vector>

int main() {
    assert(sumar_pares(std::vector<int>{1, 2, 3, 4}) == 6);
    assert(sumar_pares(std::vector<int>{1, 3, 5}) == 0);
    return 0;
}
