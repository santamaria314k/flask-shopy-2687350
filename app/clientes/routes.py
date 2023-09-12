from flask import render_template,redirect,flash
from . import clientes
import app
from .forms import NewClienteForm,EdictClienteForm

# Rutas del módulo "clientes"

@clientes.route("/listarcli")
def listarcli():
    clientes = app.models.Cliente.query.all()
    return render_template("listar_clientes.html", clientes=clientes)



@clientes.route("/nuevocli", methods=["GET", "POST"])
def nuevocli():
    form = NewClienteForm()
    if form.validate_on_submit():
        c = app.models.Cliente()
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
    #return os.getcwd()        
        flash("producto registrado correctamente")
        return redirect("/clientes/listarcli")

    return render_template("new_cliente.html", form=form)

       
       
       
       
       
    
@clientes.route("/editar/<cliente_id>",methods=['GET','POST'])
def editar(cliente_id):
    c=app.models.Cliente.query.get(cliente_id)
    form=EdictClienteForm(obj = c)
    if form.validate_on_submit():
            form.populate_obj(c)
            app.db.session.commit()
            flash("producto ACTUALIZADO correctamente")
            return redirect("/clientes/listarcli")
    return render_template("new_cliente.html",operacion="Actualizar",form=form)





@clientes.route('/eliminar/<cliente_id>')
def eliminar(cliente_id):
    c=app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(c)
    app.db.session.commit()
    flash("CLIENTE eliminado")
    return redirect("/clientes/listarcli")
 
       
       