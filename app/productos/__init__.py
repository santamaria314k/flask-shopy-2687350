from flask import Blueprint


productos=Blueprint('productos',__name__,url_prefix='/productos',template_folder='templates')


#vincular archivo de rutras
from . import routes

