from flask import Blueprint, jsonify
from ..web.controllers import file_controller
from ..web.controllers import auth


web_bp = Blueprint('web_home', __name__)
# Lista para simular el almacenamiento de usuarios
@web_bp.route('/')
def home():
    return jsonify('Bienvenido al app ---WEB---')

@web_bp.route('/process_file')
def process_file():
    read_file = file_controller.leer_csv()
    return jsonify(read_file)

@web_bp.route('/listar')
def listar():
    auth_list = auth.lists()
    return jsonify(auth_list)

@web_bp.route('/register', methods=['GET', 'POST'])
def register_post():
    register = auth.register()
    return jsonify(register)