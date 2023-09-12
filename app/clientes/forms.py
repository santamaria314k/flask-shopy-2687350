from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class ClienteForm():
    username = StringField("Nombre del Usuario", validators=[InputRequired(message="Ingrese el nombre del usuario")])
    password = PasswordField('CONTRASEÑA', validators=[
        InputRequired(message="Introduzca CONTRASEÑA"),
        Length(min=1, max=10, message="La contraseña debe tener entre 1 y 10 caracteres")
    ])
    email = StringField("Correo Electrónico", validators=[Email(message="Ingrese un correo electrónico válido")])



class NewClienteForm (FlaskForm,ClienteForm):


  submit=SubmitField("Guardar")
  
  
  
class EdictClienteForm(FlaskForm,ClienteForm):
    submit=SubmitField("Actualizar cliente")
