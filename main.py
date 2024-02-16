from flask import Flask, request, render_template
from io import open

import forms

app = Flask(__name__)

@app.route("/")
def cargarIndex():
    return render_template("index.html")

@app.route("/alumnos", methods=["GET", "POST"])
def cargarAlumnos():
    alumno_form = forms.UserForm(request.form)
    
    if request.method == "POST" and alumno_form.validate():
        nombre = alumno_form.nombre.data
    
    return render_template("alumnos.html", form = alumno_form)

@app.route("/guardar-diccionario", methods=["GET", "POST"])
def cargarGuardarDiccionario():
    form = forms.DiccionarioForm(request.form)
    
    if request.method == "POST" and form.validate():
        palabraIngles = form.palabraIngles.data
        palabraEspaniol = form.palabraEspaniol.data
        
        archivoDiccionario = open("diccionario.txt", "a")
        archivoDiccionario.write(f"{palabraIngles}:{palabraEspaniol}\n")
        
        return render_template("diccionario.html", form = form, resultado = "Palabra guardada correctamente")
    
    return render_template("diccionario.html", form = form)

@app.route("/consultar-diccionario", methods=["GET", "POST"])
def cargarConsultarDiccionario():
    form = forms.consultarForm(request.form)
    
    if request.method == "POST" and form.validate():
        palabraTraducir = form.palabraTraducir.data
        idiomaConsultar = form.idiomaConsultar.data
        
        archivoDiccionario = open("diccionario.txt", "r")
        
        traduccionEncontrada = ""
        print(palabraTraducir)
        
        for lineas in archivoDiccionario.readlines():
            traduccion = lineas.rstrip().split(":")
            print(traduccion[0])
            
            if(idiomaConsultar == "1"):
                # INGLES
                if(palabraTraducir == str(traduccion[0])):
                    traduccionEncontrada = str(traduccion[1])
                    break
            else:
                # ESPAÑOL
                if(palabraTraducir == str(traduccion[1])):
                    traduccionEncontrada = str(traduccion[0])
                    break
                
        if traduccionEncontrada == "":
            resultado = "No se encontro ninguna traducción"
        else:
            resultado = f"La traducción de {palabraTraducir} es {traduccionEncontrada}"
        
        return render_template("consultar.html", form = form, resultado = resultado)
    
    return render_template("consultar.html", form = form)

@app.route("/distancia-entre-puntos", methods=["GET", "POST"])
def cargarDistancia():
    formulario = forms.UserForm(request.form)
    
    if request.method == "POST":
        nombre = formulario.nombre.data
        email = formulario.email.data
        materias = formulario.materias.data
        
        print(materias)
    
    return render_template("alumnos.html", form = formulario)

@app.route("/maestros")
def cargarMaestros():
    return render_template("maestros.html")

@app.route("/datos")
def cargarInicio():
    return "<h1>Hola mundo</h1>"

@app.route("/hola")
def cargarHola():
    return "<h1>Saludos desde Hola - Modificado</h1>"

@app.route("/saludo")
def cargarSaludo():
    return "<h1>Saludos desde Saludo</h1>"

# Usando parametros
@app.route("/nombre/<string:nom>")
def cargarNombre(nom):
    return f"<h1>Bienvenido, {nom}</h1>"

@app.route("/numero/<int:n1>")
def cargarNumero(n1):
    return f"<h1>El valor es {n1}</h1>"

@app.route("/user/<string:nom>/<int:id>")
def cargarUser(nom, id):
    return f"<h1>Eres {nom} con el id {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def realizarSuma(n1, n2):
    return f"<h1>La suma de los valores es {n1 + n2}</h1>"

@app.route("/resta/<n1>/<n2>")
def realizarResta(n1, n2):
    return f"<h1>La resta de los valores es {float(n1) - float(n2)}</h1>"

# Usando querys
@app.route("/query")
def realizarQuery():
    n1 = request.args.get('n1', type=str)

    return f"La query es esto {n1}"

# Cargando un formulario
@app.route("/multiplica", methods=["GET"])
def multiplica():
        return '''
        <form action="/multiplica" method="POST">
            <label>N1:</label>
            <input type="number" name="n1"/>
            
            <label>N2:</label>
            <input type="number" name="n2"/>
            
            <input type="submit"/>
        </form>
        '''

# Utilizando render_template
@app.route("/formulario1")
def cargarFormulario1():
    return render_template("formulario1.html")

# Usando método POST
@app.route("/resultado", methods=["POST"])
def cargarResultado():
    num1 = int(request.form.get("n1"))
    num2 = int(request.form.get("n2"))
    
    return f"<h1>La multiplicación de los números {num1} * {num2} es: {num1 * num2}</h1>"

# Método Main
if __name__ == "__main__":
    app.run(debug=True, )