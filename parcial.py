def mi_funcion(arr):
    if len(arr)<= 1:
        return True
    else:
        return arr[0] <= arr[1] and mi_funcion(arr[1:])
    
print(mi_funcion([1,2,3,4])) #True
print(mi_funcion([4,2,6,1])) #True
print(mi_funcion([1,2,2,3,4])) #False
print('algoooooooooo')
class Yyy:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

zzz = Yyy(1)
print(zzz.x)
zzz.x = 2
print(zzz.x)

print('algoooooooooo')
def mi_funcion(s):
    if len(s) == 1:
        return 0
    else:
        return (1 if s[0] in 'aeiouAEIOU' else 0) + mi_funcion(s[1:])
    
print(mi_funcion('python')) #2
print(mi_funcion('holas')) #2
print(mi_funcion('algoritmos')) #3
