from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola():
    return "<h1>Hola mundo</h1>"

if __name__ == "__main__":
    app.run()