"""
Implemente la clase Lamparita, que sirva para representar el estado de encendido
de una lamparita (encendido o apagado). Defina, asimismo, dos métodos que
permitan encender y apagar la luz de la lamparita y otro que indique en qué
estado se encuentra. La lamparita inicialmente está apagada
"""

class Lamparita:
    def __init__(self):
        self.estado = False
        
    def encender(self):
        self.estado = True
        
    def apagar(self):
        self.estado = False
        
    def esta_encendida(self):
        if self.estado:
            return "La lamparita está encendida"
        return "La lamparita está apagada"
    
# Test
lamparita = Lamparita()

print(f'Estado inicial_ {lamparita.esta_encendida()}')
lamparita.encender()
print(f'Prendo la lamparita: {lamparita.esta_encendida()}')
lamparita.apagar()
print(f'Apago la lamparita: {lamparita.esta_encendida()}')
