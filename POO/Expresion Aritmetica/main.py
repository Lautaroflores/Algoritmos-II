from expresionAritmetica import *

if __name__ == "__main__":
    expresion =Suma(Producto(Constante(3), Constante(5)), Negacion(Incremento(Constante(2))))
    resultado = expresion.evaluar()
    print(f'{expresion} = {resultado}')
    
    
    
    
    
