from flask import render_template
from . import productos
import app
from .forms import Registrarproductoform

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
        app.db.session.add(p)
        app.db.session.commit()
        return "producto registrado"  
    return render_template("new.html", form=form)

    