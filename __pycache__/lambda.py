people = [
    { "name": "Harry", "house":"Gryffindor"},
    { "name": "Cho", "house":"Revenclaw"},
    { "name": "Draco", "house":"Slytherin"}
]

def f(person):
    return person["house"]

people.sort( key=f)
print (people)

#lambda
people.sort(key=lambda person: person["name"])
print (people)

# example lambda function
suma = lambda x, y: x + y

# Uso de la función lambda
resultado = suma(3, 5)
print(resultado)

# example lambda function
calcular_media = lambda secuencia: sum(secuencia) / len(secuencia) if len(secuencia) > 0 else None

# Uso de la función lambda
secuencia1 = [1, 2, 3, 4, 5,6,7,8,9,10]
secuencia2 = []  # Una lista vacía

media1 = calcular_media(secuencia1)
media2 = calcular_media(secuencia2)

print(media1)  # Salida esperada: 3.0 (la media de 1, 2, 3, 4, 5 es 3)
print(media2)  # Salida esperada: None (la secuencia2 está vacía, no se puede calcular la media)
