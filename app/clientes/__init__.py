from flask import Blueprint




clientes=Blueprint('clientes',__name__,url_prefix='/clientes',template_folder='templates')

#vincular archivo de rutras
from . import routes
