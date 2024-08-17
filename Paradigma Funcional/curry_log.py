'''
A lo largo de nuestro programa es posible que necesitemos almacenar
información de interés en el log de ejecución. A efectos prácticos, nuestro destino
de log será la consola, por lo que podemos utilizar simplemente un print() para
registrar un mensaje de log.
Implementar una función log currificada que permita registrar un mensaje de log y
el tipo, que puede ser error, alerta o información. 
'''

from pymonad.tools import curry

@curry(2)
def log(tipo: str, mensaje: str) -> str:
    return f'[{tipo}] {mensaje}'

if __name__ == '__main__':
    log_error = log('Error')
    
    print(log_error('Error en la conexión a la base de datos'))
    
