from flask import Flask
from src.bff.routes import web_bp, mobile_bp
from src.importacion.database.connection import db, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from config import get_config
from flask_cors import CORS
app = Flask(__name__)

# cors = CORS(app, resources={r"/web/*": {"origins": "*"}})
CORS(app)

config = get_config()
app.config.from_object(config)

#CONEXION BASE DE DATO
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


with app.app_context():
     db.init_app(app)
#SQLAlchemy(app)



# Registra el Blueprint 'WEB'
route_web = '/web'
route_mobile = '/api'
app.register_blueprint(web_bp, url_prefix   = route_web)


#APIS
app.register_blueprint(mobile_bp, url_prefix= route_mobile)


