'''
Definir la clase ExpresionAritmetica, que permita representar constantes
numéricas enteras, operaciones binarias de suma y producto, y operaciones
unarias de negación aritmética, incrementar y decrementar. Toda expresión
deberá poder evaluar el resultado de la expresión, retornando el valor entero
resultante. Definir tantas subclases como posibilidades existan de armar
expresiones aritméticas.
'''

class ExpresionAritmetica:
        
        def __init__(self):
            pass
        
        def evaluar(self) -> int:
            pass
        
        def __str__(self):
            pass
        
class Constante(ExpresionAritmetica):
        
        def __init__(self, valor: int):
            self.valor = valor
            
        def evaluar(self) -> int:
            return self.valor
        
        def __str__(self):
            return str(self.valor)
        
class Suma(ExpresionAritmetica):
            
    def __init__(self, exp1: ExpresionAritmetica, exp2: ExpresionAritmetica):
        self.exp1 = exp1
        self.exp2 = exp2
        
    def evaluar(self) -> int:
        return self.exp1.evaluar() + self.exp2.evaluar()
    
    def __str__(self):
        return f'({self.exp1} + {self.exp2})'
    
class Producto(ExpresionAritmetica):
    
    def __init__(self, exp1: ExpresionAritmetica, exp2: ExpresionAritmetica):
        self.exp1 = exp1
        self.exp2 = exp2
        
    def evaluar(self) -> int:
        return self.exp1.evaluar() * self.exp2.evaluar()
    
    def __str__(self):
        return f'({self.exp1} * {self.exp2})'
    
class Negacion(ExpresionAritmetica):
    
    def __init__(self, exp: ExpresionAritmetica):
        self.exp = exp
        
    def evaluar(self) -> int:
        return -self.exp.evaluar()
    
    def __str__(self):
        return f'(-{self.exp})'
    
class Incremento(ExpresionAritmetica):
    
    def __init__(self, exp: ExpresionAritmetica):
        self.exp = exp
        
    def evaluar(self) -> int:
        return self.exp.evaluar() + 1
    
    def __str__(self):
        return f'({self.exp} + 1)'
    
class Decremento(ExpresionAritmetica):
    
    def __init__(self, exp: ExpresionAritmetica):
        self.exp = exp
        
    def evaluar(self) -> int:
        return self.exp.evaluar() - 1
    
    def __str__(self):
        return f'({self.exp} - 1)'
    

    