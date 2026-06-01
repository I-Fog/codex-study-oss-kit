import unittest

from src.ejercicio import sumar_pares


class SumarParesTest(unittest.TestCase):
    def test_suma_solo_pares(self) -> None:
        self.assertEqual(sumar_pares([1, 2, 3, 4]), 6)

    def test_lista_sin_pares(self) -> None:
        self.assertEqual(sumar_pares([1, 3, 5]), 0)


if __name__ == "__main__":
    unittest.main()
