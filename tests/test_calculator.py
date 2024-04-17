import unittest
from calculator import Calculator

class Test_calculator(unittest.TestCase):
    
    @test
    def test_soma(self):
        c = Calculator(2, 8)
        self.assertEqual(c.soma(), 10)
        
    def test_soma_2(self):
        c = Calculator(-3, 7)
        self.assertEqual(c.soma(), 4)

    def teste_soma_3(self):
        c = Calculator(-3, -4)
        self.assertEqual(c.soma(), -7)

    def teste_soma_4(self):
        c =  Calculator(0, 10)
        self.assertEqual(c.soma(), 10)