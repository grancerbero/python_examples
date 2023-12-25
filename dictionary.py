# Crear un diccionario vacío
mi_diccionario = {}

# Crear un diccionario con elementos
diccionario_valores = {'clave1': 10, 'clave2': 20, 'clave3': 30}
valor = diccionario_valores['clave2']
print(valor)
diccionario_valores['clave4'] = 40
diccionario_valores['clave4'] = 80

print (diccionario_valores)


for clave, valor in diccionario_valores.items():
    print(f'Clave: {clave}, Valor: {valor}')

# Eliminar la clave 'clave3' y su valor asociado
del diccionario_valores['clave3']

#recorrer todas las claves y valores
for clave, valor in diccionario_valores.items():
    print(f'Clave: {clave}, Valor: {valor}')


# Verificar si 'clave2' está en el diccionario
existe = 'clave2' in diccionario_valores
print (existe)

# Obtener todas las claves
claves = diccionario_valores.keys()
print (claves)


# Obtener todos los valores
valores = diccionario_valores.values()
print (valores)

print (type(valores))