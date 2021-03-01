# CREAR UNO NOSOTROS
# DESCARGAR DESDE INTERNET
#       https://pypi.org/
# MODULOS DESDE LA PROPIA BLIBLIOTECA DE PYTHON
#       https://docs.python.org/3/py-modindex.html
#
#Modulos preconstruidos



#Fechas
#       https://docs.python.org/3/library/datetime.html#module-datetime
#import datetime
from datetime import timedelta,date
#importar el modulo que costrui
from operaciones import sumar,restar,multip
from colorama import Fore, Back, Style, init
init(convert=True)
#Fecha actual
print(f"Fecha actual: {date.today()}")

#Minutos a horas
print( f"Convierte 100 minutos a horas: {timedelta(minutes=100)}  ")


print(f"la suma es: {sumar(1,5)}")
print(f"la restar es: {restar(1,5)}")
print(f"la multip es: {multip(1,5)}")


#python --version
#   Sirve para interpretar codigo
#pip --version
#   Sirve para instalar modulos de terceros
#pip install colorama //poner colore a la terminar


#---------colorama-------------
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


#Modulo Flask
#
# Flask es un marco de aplicación web WSGI ligero. Está diseñado para que la puesta en marcha sea rápida y sencilla,
# con la capacidad de escalar a aplicaciones complejas. Comenzó como una simple envoltura alrededor de Werkzeug y
# Jinja y se ha convertido en uno de los marcos de aplicaciones web de Python más populares. Flask ofrece sugerencias,
# pero no impone ninguna dependencia o diseño del proyecto. Depende del desarrollador elegir las herramientas y bibliotecas
# que desea utilizar. Hay muchas extensiones proporcionadas por la comunidad que facilitan la adición de nuevas funciones.
#   https://pypi.org/project/Flask/
#   pip install Flask


#Modulo django
#https://pypi.org/search/?q=django



#Modulo tkinter
# para aplicaciones de interfaz grafica escritorio
#https://pypi.org/search/?q=tkinter&o=

