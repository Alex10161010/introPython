#estas no cambian su valor
#son mucho mas rapido que las listas
#   se ocupan para mantener mas seguro el codigo y rapido
datos = (1,2,3,4)
meses = ('Enero', 'Febrero', 'Marzo', 'Abril')
print (type(datos))
print (meses[0])

#eliminar tupla
del meses
print (meses)

#en donde se ocupa
locations ={
    (35.151,58.515):"Tokyo",
    (35.151,55.515):"Mexico",
}