from wtforms import Form
from wtforms import StringField, TextAreaField, TextField, SelectField, RadioField
from wtforms import EmailField

class UserForm(Form):
    nombre = StringField("nombre")
    email = EmailField("correo")
    primerApellido = TextField("primerApellido")
    segundoApellido = TextField("segundoApellido")
    materias = SelectField(choices=[('Español', "ESP"),("Matemáticas", "Mat"), ("Ingles", "ING")])
    radios = RadioField("curso", choices=[("1","1"), ("2","2"), ("3","3"), ("4","4"), ("5","5")])