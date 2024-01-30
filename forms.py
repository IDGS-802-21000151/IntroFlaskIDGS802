from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre = StringField("nombre", [
        validators.DataRequired()
    ])
    email = EmailField("correo")
    materias = SelectField(choices=[('Español', "ESP"),("Matemáticas", "Mat"), ("Ingles", "ING")])
    radios = RadioField("curso", choices=[("1","1"), ("2","2"), ("3","3"), ("4","4"), ("5","5")])