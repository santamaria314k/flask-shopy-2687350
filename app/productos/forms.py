
from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField

 
class Registrarproductoform(FlaskForm):
   
  nombre=StringField("Nombre del producto")
  precio=StringField("precio del producto")
  submit=SubmitField()