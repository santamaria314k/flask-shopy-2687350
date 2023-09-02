from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField,IntegerField
from wtforms.validators import InputRequired,NumberRange
from flask_wtf.file import FileField,FileRequired,FileAllowed

class Registrarclienteform(FlaskForm):
   
  username=StringField("Nombre del Usuario", validators = [InputRequired(message="ingrese el nombre del usuario")])
  password=StringField('  Contraseña',validators=[InputRequired(message="introdusca la contraseña")])
  email=StringField("Correo Electronico", validators = [InputRequired(message="Ingrese el correo Electronico")])

  submit=SubmitField("Guardar")
  
  