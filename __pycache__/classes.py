class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2,8)
print (p.x)
print (p.y)
        

# Crear un objeto Point
punto_original = Point(1, 2)

# Asignar ese objeto a otra variable
punto_referencia = punto_original

# Modificar el objeto a través de una de las variables
punto_referencia.x = 10

# Imprimir los valores desde ambas variables
print(punto_original.x, punto_original.y)  # Salida: 10 2
print(punto_referencia.x, punto_referencia.y)  # Salida: 10 2

import copy

# Crear una copia superficial del objeto
punto_copia_superficial = copy.copy(punto_original)
punto_copia_superficial.x =20;
print (punto_copia_superficial.x);

# Crear un nuevo objeto con los mismos valores
punto_nuevo = Point(punto_original.x, punto_original.y)
print (punto_nuevo.x)



