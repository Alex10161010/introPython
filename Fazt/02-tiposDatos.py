# Tipos de datos
#String
#   "Hola"      'Hola'    """Hola"""      '''Hola'''
#Numbers
#   integer         float
#


#String
print(type("Hola mundo que tipo es"))
print("Hola primera forma")
print('Hola segundo forma')
print("""Hola tercera forma""")
print('''Hola cuarto forma''')
#Unir palabras (Concatenar)
print("Adios" + " Mundo")


#Numeros
print("------Numeros-------")
# int
print(type(30))
#   float
print(type(30.5))

# Boolean
# para definir tipos de estado
print("------Boolean-------")
print(type(True))
print(type(False))


#List
#   esta conformada por elementos
#   puede estar vacias
#Lista de enteros
print("------Listas-------")
print(type([10, 20, 30, 55]))
print(type(['Hola', 'Bye', 'Adios', 'Ok']))
print(type([10, 'Hola', 30, 'Adios']))


#Tuples
# Se utiliza en datos que no cambian
# Tambien se le conoce como inmutable
print("------Tuples-------")
print(type((10,20, 30, 55)))


#Dictorion  dicionarios
#   agrupar distintos tipos de datos con un nombre clave es igual al json
print("------Dictorion-------")
print(type({
    "nombre": "Ryan",
    "apellido": "Morales",
    "apodo": "Alex",
    "edad":28
}))


#Tipo de dato No definido
print("------None-------")
print(type(None))