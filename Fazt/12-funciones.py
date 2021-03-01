#funciones

#Definir una funcion
def saludar(nombre="Persona"):
    print(f"Hola {nombre}")


#retornar un valor
def sumar(numeroUno, numeroDos):
    return numeroUno + numeroDos



# saludar("Elias Alejandro")
# saludar()

#print(sumar(9,15))


#tipo de funcion lambda
#   son funciones anonimas que toman un numero de elementos Y RETORNA ALGO

getAdd = lambda numero1,numero2: numero1+numero2
print(getAdd(151,182))