

from app import db
from datetime import datetime






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
