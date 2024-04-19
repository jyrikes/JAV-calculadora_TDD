import unittest
from calculator import Calculator

class Test_calculator(unittest.TestCase, Calculator):
    
    def setUp(self):
        self.calculadora = Calculator()
        
    def test_soma(self):
        self.assertEqual(self.soma(2, 8), 10)
    
    # testes para o método raiz_quadrada
    def test_raiz_quadrada_1(self):
        self.assertEqual(self.raiz_quadrada(9), 3)
    
    def test_raiz_quadrada_2(self):
        self.assertEqual(self.raiz_quadrada(0), 0)

    def test_raiz_quadrada_3(self):
        self.assertEqual(self.raiz_quadrada(-32), "Não é possível calcular a raiz quadrada de um número negativo") 
    
    # testes para o método fatorial
    def test_fatorial_1(self):
        self.assertEqual(self.fatorial(5), 120)

    def test_fatorial_2(self):
        self.assertEqual(self.fatorial(0), 1)

    def test_fatorial_3(self):
        self.assertEqual(self.fatorial(-5), "Não é possível calcular o fatorial de um número negativo")

    # testes para o método resto_divisao
    def test_resto_divisao_1(self):
        self.assertEqual(self.resto_divisao(10, 2), 0)

    def test_resto_divisao_2(self):
        self.assertEqual(self.resto_divisao(10, 3), 1)
    
    def test_resto_divisao_3(self):
        self.assertEqual(self.resto_divisao(10, 0), "Não é possível dividir por zero")

    def test_resto_divisao_4(self):
        self.assertEqual(self.resto_divisao(7, 4), 3)

if __name__ == '__main__':
    unittest.main()