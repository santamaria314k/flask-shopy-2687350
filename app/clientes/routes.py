from flask import render_template
from . import clientes
import app
from .forms import Registrarclienteform

# Rutas del módulo "clientes"

@clientes.route("/listarcli")
def listarcli():
    clientes = app.models.Cliente.query.all()
    return render_template("listar_clientes.html", clientes=clientes)

@clientes.route("/nuevocli", methods=["GET", "POST"])
def nuevocli():
    form = Registrarclienteform()
    if form.validate_on_submit():
        c = app.models.Cliente()
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
    #return os.getcwd()        
        return "Cliente registrado"  

    return render_template("new_cliente.html", form=form)

    