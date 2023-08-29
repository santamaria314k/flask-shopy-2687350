from flask import render_template
from . import productos
import app
from .forms import Registrarproductoform
import os

# Rutas del módulo "productos"

@productos.route("/listar")
def listar():
    productos = app.models.Productos.query.all()
    return render_template("index.html", productos=productos)

@productos.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    form = Registrarproductoform()
    if form.validate_on_submit():
        p = app.models.Productos()
        form.populate_obj(p)
        p.imagen= form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
    #return os.getcwd()
        
        #Extraer el objeto fileStorage
        file= form.imagen.data
        file.save(os.path.abspath(os.getcwd() + "/app/productos/imagenes/"
                                  + form.imagen.data.filename))
        return "producto registrado"  

    return render_template("new.html", form=form)

    