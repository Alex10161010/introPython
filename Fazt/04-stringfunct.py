nombre= "Elias Alejandro"
#print(nombre)

#El dir nos enseña todos los metodos que podemos ocupar con un tipo de dato
#       print(dir(nombre))


#upper      Mayusculas
#lower      Minuscula
#swapcase   La primera letra en Minuscula
#capitalize   La primera letra en Mayuscula
#   print(nombre.upper())
#   print(nombre.lower())
#   print(nombre.swapcase())
#   print(nombre.capitalize())


#remplace
#       Reemplazar la palabra
#   nombre = nombre.replace("Elias", "Alex").lower()


#count
#       cuantas veces existe una palabra o una letra
#   contar_a= nombre.count('Morales')
#print('La letra a existe:', contar_a)


#starswith
#       Compruebe si la cadena comienza con "Elias" devuelve un True || False
#existe = nombre.startswith("Elias")
#print('existe al comienzo Elias:', existe)


#endswith
#       Compruebe si la cadena termina con
#existe = nombre.endswith("Mancera")
#print('termina la cadena con Mancera:', existe)


#spli
#       Divida una cadena en una "lista" donde cada palabra es un elemento de LISTA
#stringDato= "elias#aleajndro#28#rango"
#dividir = stringDato.split('#')
#print(dividir)
#print(dividir[2])


#find
#       El find() método encuentra la primera  posicion de aparición del valor especificado. dentro de la cadena
#       devuelve el indice y si no se encuetra devuelve -1
#stringDato= "elias aleajndro edad 28 rango 2"
#buscar_posic = stringDato.find('s')
#print('La primera posicion de la letra S esta en: ',buscar_posic)


#len
#        devuelve la longitud de la cadena
#stringDato= "elias aleajndro edad 28 rango 2"
#longitud_cadena = len(stringDato)
#print('La longitud de la cadena es: ',longitud_cadena)


#index
#       método devuelve la posición en la primera aparición del valor especificado.
#frutas = ['manzana', 'banana', 'pera','guayaba']
#indice = frutas.index("guayaba")
#print('¿Cuál es la posición del valor "guayaba": ',indice)


#isnumeric
#       devuelve True si todos los caracteres de una cadena son numéricos. Si no, devuelve False.
#s = '1242323'
#print(s.isnumeric())


#isalpha
#       evuelve True si todos los caracteres de la cadena son alfabetos. Si no, devuelve False.
#name = "Monica"
#print(name.isalpha())


#
#      Maneras de Concatenación
block_notas1 = "Estudiar React"
block_notas2 = "Estudiar Python"
block_notas3 = "Terminar Credito y CV"
numero_tarea = 56;

print("Mis notas son las siguientes: " + block_notas1)
print(f"Mis notas son las siguientes: {block_notas2}")
print(f"Numero de tareas son: {numero_tarea}")
print("Cosas por hacer: {0}" .format(block_notas3))