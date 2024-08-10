'''
Implemente la clase Fecha, que permita representar una terna de día, mes y año,
todos de tipo entero. Programar un método que determine si una fecha es mayor
a otra. Programar la sobrecarga del método __str__ y __gt__(operador mayor).
'''
class Fecha:
    def __init__(self, dia, mes, anio):
        
        if not isinstance(dia, int):
            raise TypeError(f'La fecha debe estar compuesta de numeros de tipo entero, se recibió día: {type(dia).__name__}')
        if not isinstance(mes, int):
            raise TypeError(f'La fecha debe estar compuesta de numeros de tipo entero, se recibió mes: {type(mes).__name__}')
        if not isinstance(anio, int):
            raise TypeError(f'La fecha debe estar compuesta de numeros de tipo entero, se recibió año: {type(anio).__name__}')
  
        self.dia = dia
        self.mes = mes
        self.anio= anio
        
    def __str__(self):
        return f'La fecha es {self.dia}/{self.mes}/{self.anio}'
    
    def __gt__(self, other):
        if self.anio > other.anio:
            return True
        elif self.mes > other.mes:
            return True
        elif self.dia > other.dia:
            return True
        else:
            return False
        
if __name__ == '__main__':  
    try:
        fechita= Fecha(31,12,2024)
        print(f'Primer fecha: {fechita}')
        
        fechita2 = Fecha(30,12,2024)
        print(f'Segunda fecha: {fechita2}')
        
        
        print(f'Comparación de fechas: {fechita > fechita2}')    
        
    except Exception as e:
        print(e)
            