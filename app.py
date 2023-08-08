# dependencias del proyecto
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# crear el objeto de aplicación
app = Flask(__name__)
#configurar app para conectarse a bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3307/flask-shopy-2687350'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# crear el objeto sqlalchemy
db = SQLAlchemy(app)
#crear el objeto de migracion y activarlo
migrate = Migrate(app , db)

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
    imagen =db.Column(db.String(64))



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




