import unittest
from calculator import Calculator

class Test_calculator(unittest.TestCase, Calculator):
    
    def setUp(self):
        self.calculadora = Calculator()
        
    def test_soma(self):
        self.assertEqual(self.soma(2, 8), 10)
        
    def test_divisao_inteira(self):
        self.assertEqual(self.divisao(10,5,2),2)
    
    def test_divisao_float(self):
        self.assertEqual(self.divisao(1.2,0.1,2),12)
    
    def test_divisao_inteira_sem_precisao(self):
       self.assertEqual(self.divisao(10,5),2)
       
    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.divisao(10,0)
    
        

if __name__ == '__main__':
    unittest.main()