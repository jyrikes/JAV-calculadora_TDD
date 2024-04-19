class Calculator:
    
    def __init__(self) -> None:
        pass
    
    def soma(self, number1, number2):
        try:
            number1 = float(number1)
            number2 = float(number2)
        except:
            raise ValueError("Não é possivel fazer soma de algo diferente de um número")
        
        return number1 + number2
    
    def subtracao(self, number1, number2):
        try:
            number1 = float(number1)
            number2 = float(number2)
        except:
            raise ValueError("Não é possivel fazer subtração de algo diferente de um número")
        
        return number1 - number2
    
    def multiplicacao(self, number1, number2):
        try:
            number1 = float(number1)
            number2 = float(number2)
        except:
            raise ValueError("Não é possivel fazer multiplicação de algo diferente de um número")
        
        #limitando o resultado a apenas duas casas decimais 
        return round(number1 * number2, 2)
        

    
    def divisao(self, dividendo,divisor,precisao = 1):
        
        if divisor == 0 :
            raise ZeroDivisionError
        
        elif isinstance(dividendo,str) or isinstance(divisor,str):
            raise ValueError
        
        elif dividendo is None or divisor is None:
            raise ValueError
        
        elif isinstance(dividendo, float) or isinstance(divisor,float):
            fator_precisao = 10**precisao
            dividendo = dividendo * fator_precisao
            divisor = divisor * fator_precisao
            
        return dividendo / divisor
    
    def divisao_inteira(self,dividendo, divisor):
        
        return int(self.divisao(dividendo,divisor))
    
    
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
    
    
    
    
    
        