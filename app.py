# dependencias del proyecto
from flask import Flask ,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from config import Config

# crear el objeto de aplicación
app = Flask(__name__)
#configurar app para conectarse a bd
app.config.from_object(Config)

#configurar bootstrap con app
bootstrap = Bootstrap(app)

# crear el objeto sqlalchemy
db = SQLAlchemy(app)
#crear el objeto de migracion y activarlo
migrate = Migrate(app , db)

#Crear el formulario de registro de productos
class RegistroProductosForm(FlaskForm):
    nombre=StringField('Nombre del producto')
    precio=StringField('Precio del Producto')
    submit = SubmitField('Guardar producto')


##Modelos <<entities>>
class Cliente(db.Model):
    __tablename__="clientes"
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    email = db.Column(db.String(120))

class Productos(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(64))
    precio =db.Column(db.Float)
    imagen =db.Column(db.String(255) ,nullable=True)



class Venta(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer,primary_key=True)
    fecha=db.Column(db.DateTime , default= datetime.utcnow)
    cliente_id =db.Column(db.Integer,db.ForeignKey('clientes.id'))





class Detalle(db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer,primary_key=True)
    producto_id =db.Column(db.Integer,db.ForeignKey('productos.id'))
    venta_id =db.Column(db.Integer,db.ForeignKey('ventas.id'))
    cantidad =db.Column(db.Integer())

#Relaciones  <<entities>>







@app.route('/productos/registrar' , methods = ['GET' , 'POST'])
def registrar():
    form = RegistroProductosForm()
    p = Productos()
    if form.validate_on_submit():
        #crear un objeto cliente
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        return "producto registrado"
    return render_template('registrar.html' ,
                          form = form )    