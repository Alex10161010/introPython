from flask import Flask,render_template

#la variable que servira para controlar la aplicacion
app = Flask(__name__)

#configurar ruta
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contacto')
def ruta_contacto():
    return render_template('contacto.html',)

@app.route('/lenguajes')
def ruta_lenguajes():
    mylenguajes=("PHP 7","JavaScript","C#", "Java","Python")
    return render_template('lenguajes.html',lenguajes=mylenguajes)

#levantamiento de la aplicacion web
#       debug=True => diciendole al servidor que estoy debug y reinici cuando exista un cambio
#       port=5017 => diciendole el puerto en el que se desea
if __name__ =='__main__':
    app.run(debug=True, port=5017)

#flask ocupa un motor de plantillas Jinja2 es el mismo que ocupa django
#este nos va a permitir procesar datos y la reutilizacion de plantillas
#