from flask import render_template,redirect,flash,render_template
from . import productos
import app
from .forms import NewProductForm,EdictProductForm
import os

# Rutas del módulo "productos"

@productos.route("/listar")
def listar():
    productos = app.models.Productos.query.all()
    return render_template("index.html", productos=productos)

@productos.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    form = NewProductForm()
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
        flash("producto registrado correctamente")
        return redirect("/productos/listar")  

    return render_template("new.html",operacion="Nuevo", form=form)

    
    
    
@productos.route("/editar/<producto_id>",methods=['GET','POST'])
def editar(producto_id):
    p=app.models.Productos.query.get(producto_id)
    form=EdictProductForm(obj = p)
    if form.validate_on_submit():
            form.populate_obj(p)
            app.db.session.commit()
            flash("producto ACTUALIZADO correctamente")
            return redirect("/productos/listar")
    return render_template("new.html",operacion="Actualizar",form=form)





@productos.route('/eliminar/<producto_id>')
def eliminar(producto_id):
    p=app.models.Productos.query.get(producto_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("producto eliminado")
    return redirect("/productos/listar")
 