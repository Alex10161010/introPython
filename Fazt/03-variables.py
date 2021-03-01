#variables.py
#  28/02/2021 5:57 pm
#   Es un nombre simbolico para un valor
#   En estas variable podemos guardar cual quier tipo de dato


#string
nombre = "Elias Alejandro"
#numero
edad  = 28
#lista
meses = ['Ene','Feb','Mar']
#dicionario
obj = {
    "nombre":"Elias",
    "edad": 28,
    "curos": "Fazt",
}
#No definindo
datoNoDefin = None
print(10+182)
print(nombre)
print(edad)

#case sensitive: lo que indica es que no es lo mismo la variable (nombre != Nombre)
#----------PRIMERA FORMAS DE DEFINIR UNA VARIABLE-------------#
#x=100
#book = "I Robot"
#----------SEGUNDA FORMAS DE DEFINIR UNA VARIABLE-------------#
print("----------SEGUNDA FORMAS DE DEFINIR UNA VARIABLE-------------")
x, book = 100 ,"I Robot"
print(x,book)

#PARA QUE SEA MAS LEGILEBLE EL CODIGO
#       CONVENTIONES
book_name = "I Robot" #Snake Case / por que esta separada por un sub guion
bookName = "Digital fortress"# Camel Case
BookName = "ISAAC ASIMOV"# Pascal Case

#VALORES QUE NO CAMBIAN SE LLAMAN CONSTANTE
# Por convencion se declaran en mayusculas
PI = 3.1416
MY_NAME= "Elias Alejandro"

#python es un lenguaje dinamico esto significa que las variables pueden cambiar
book_name = "I robb"
book_name = 626226