from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def cargarIndex():
    return render_template("index.html")

@app.route("/alumnos")
def cargarAlumnos():
    return render_template("alumnos.html")

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