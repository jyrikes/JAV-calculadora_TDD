import unittest
from calculator import Calculator

class Test_calculator(unittest.TestCase):
    
    def test_soma(self):
        c = Calculator()
        self.assertEqual(c.soma(2, 8), 10)
        
    def test_soma_2(self):
        c = Calculator()
        self.assertEqual(c.soma(-3, 7), 4)

    def teste_soma_3(self):
        c = Calculator()
        self.assertEqual(c.soma(-3, -4), -7)

    def teste_soma_4(self):
        c =  Calculator()
        self.assertEqual(c.soma(0, 10), 10)

    def teste_subtracao(self):
        c = Calculator()
        self.assertEqual(c.subtracao(2, 8), -6)

    def teste_subtracao_2(self):
        c = Calculator()
        self.assertEqual(c.subtracao(-3, 7), -10)

    def teste_subtracao_3(self):
        c = Calculator()
        self.assertEqual(c.subtracao(-3, -4), 1)

    def teste_subtracao_4(self):
        c = Calculator()
        self.assertEqual(c.subtracao(0, 10), -10)

if __name__ == '__main__':
    unittest.main()