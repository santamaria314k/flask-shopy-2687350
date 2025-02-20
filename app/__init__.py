from flask import Flask ,render_template
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from .mi_blueprint import mi_blueprint
from app.productos import productos
from app.clientes import clientes

            #OBJETOS 

# crear el objeto de aplicación
app = Flask(__name__)



#configurar app para conectarse a bd desde config
app.config.from_object(Config)



# crear el objeto sqlalchemy
db = SQLAlchemy(app)
#crear el objeto de migracion y activarlo
migrate = Migrate(app , db)



#configurar bootstrap con app (objeto)
bootstrap = Bootstrap(app)



#Traer los modelos

from .models import Productos,Cliente,Venta,Detalle


#ruta de prueva
#de la masterpage
@app.route("/master")
def master():
    return render_template("base.html")


#registrar el nuevo modulo
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)
app.register_blueprint(clientes)


