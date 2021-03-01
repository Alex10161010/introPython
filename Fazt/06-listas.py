#Listas

demo_listas = [1 ,"hola", 1.35, True , [2121,455, 'Mundo']]
colores = ['Rojo', 'Negro', 'Naranja', 'Azul','Rojo']


# list: nos permite definir una lista
# lista_numero = list((1,3,6,8,323,30))
# print(lista_numero)
# print(type(lista_numero))


#lista vasada en un rango
#rango_lista= list (range(1,10))
#print(rango_lista)


#devuelve todos los metodos que se pueden ocupar
##print(dir(colores))


#Longitud de un arreglo
# longit_array = len(colores)
# print(f"longitud del arreglo: {longit_array}" )


#Si existe el lemento
#existe = 'pur' in(colores)
#print(f"el color negro existes: {existe}" )


#Modificar elemento de una lista
# factura = ['pan', 'huevos', 100, 1234]
# print(f"Listas--- : {factura}" )
# factura[1]= 'calvarios'
# print(f"Listas factura: {factura}")


#insertar un elemento al array de elementos
#   colores.append('Violeta')


#Insertar multiples elementos en un array
# newTuplaColor=('Morado','Plateado', 'Dorado')
# colores.extend(newTuplaColor)
# print(colores)


#insertar en una posicion en especifico un elemento
# colores.insert(1,'Violeta')
# colores.insert(len(colores),'Plateado')
# print(colores)


#quitar un elemento del array de colores
# print(colores)
# colores.pop()
# print(colores)


#quitar un elemento en especifico de array por nombre
# colores.remove('Negro')
# print(colores)


#quitar un elemento en especifico de array por index
# indice = 1
# colores.pop(indice)
# print(colores)


#ordenar alfabeticamente
# colores.sort()
# print(colores)


#obtener el indice de elemento
#print(colores.index('Naranja'))

#constar cuantas veces se repite un elemento
print(colores.count('Rojo'))