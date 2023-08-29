
from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField,IntegerField
from wtforms.validators import InputRequired,NumberRange
from flask_wtf.file import FileField,FileRequired,FileAllowed

class Registrarproductoform(FlaskForm):
   
  nombre=StringField("Nombre del producto", validators = [InputRequired(message="ingrese el nombre dle producto")])
  precio=IntegerField('precio producto',validators=[InputRequired(message="introdusca el valor del producto"),
                                                    NumberRange(message="precio fuera de RANGO ",min=10,max=100000)])
  
  
  imagen=FileField("Seleccione la imagen del  producto:",validators=[FileRequired(message="debe seleccionar una imagen"),FileAllowed(['jpg','png'],"solo se permiten imagenes")])
  submit=SubmitField("Guardar")
  
  
  
  