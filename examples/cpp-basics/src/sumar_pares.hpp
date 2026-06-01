#pragma once

#include <vector>

inline int sumar_pares(const std::vector<int>& numeros) {
    int total = 0;
    for (const int numero : numeros) {
        if (numero % 2 == 0) {
            total += numero;
        }
    }
    return total;
}
