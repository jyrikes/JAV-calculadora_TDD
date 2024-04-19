class Calculator:
    
    def __init__(self) -> None:
        pass
    
    def soma(self, number1, number2):
        return number1 + number2
    
    def subtracao(self, a, b):
        resultado = a - b
        return resultado
    
    def multiplicacao(self):
        return
    
    def divisao(self):
        return
    
    def divisao_inteira(self):
        return
    
    def potencia(self):
        return
    
    def raiz_quadrada(self, a):
        try:
            a = int(a)
        except:
            raise ValueError("Não é possível calcular a raiz quadrada de algo diferente de um número")
        if a < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo")
        return a ** 0.5
    
    def fatorial(self, a):
        try:
            a = int(a)
        except:
            raise ValueError("Não é possível calcular o fatorial de algo diferente de um número inteiro")
        if a < 0:
            raise ValueError("Não é possível calcular o fatorial de um número negativo")
        if a == 0:
            return 1
        return a * self.fatorial(a - 1)
    
    def resto_divisao(self, a, b):
        try:
            a = int(a)
            b = int(b)
        except:
            raise ValueError("Não é possível calcular o resto da divisão de algo diferente de um número inteiro")
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        return a % b
    
    
    
    
    
        