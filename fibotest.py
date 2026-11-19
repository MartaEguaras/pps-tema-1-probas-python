import unittest
from fibo import fibonacci


class ProbarFibonacci(unittest.TestCase):

  def test_fibonacci_9_elementos(self):
    # Comprobamos la secuencia para n = 9 elementos
    resultado_obtenido = fibonacci(9)
    resultado_esperado = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    self.assertEqual(resultado_obtenido, resultado_esperado)

  def test_fibonacci_11_elementos(self):
    # Comprobamos la secuencia para n = 11 elementos
    resultado_obtenido = fibonacci(11)
    resultado_esperado = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    self.assertEqual(resultado_obtenido, resultado_esperado)

  def test_fibonacci_caso_cero(self):
    # Comprobamos el caso límite de 0 elementos
    self.assertEqual(fibonacci(0), [])


if __name__ == "__main__":
  unittest.main()