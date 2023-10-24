from flask import Blueprint, jsonify, request, current_app 
import hashlib
from src.importacion.web.controllers import file_controller
from src.importacion.web.controllers import user_controller


web_bp = Blueprint('web_home', __name__)
# Lista para simular el almacenamiento de usuarios
@web_bp.before_request
def before_request_func():
    print("-"*10,"VALIDA KEY", "-"*10)
    
    api_key = request.headers.get('API-Key')
    if api_key != current_app.config['SECRET_KEY']:
        return jsonify({'message':'acceso denegado'})
    
@web_bp.app_errorhandler(404)
def page_not_found(error):
    return 'This page does not exist. MSG', 404
    

@web_bp.route('/')
def home():
    return jsonify('Bienvenido al app ---WEB BFF---')

@web_bp.route('/process_file')
def process_file():
    response = file_controller.leer_csv()
    return jsonify(response)

@web_bp.route('/user_list')
def listar():
    response = user_controller.lists()
    return jsonify(response)

@web_bp.route('/create_user', methods=['GET', 'POST'])
def create_user_post():
    response = user_controller.create_user()
    return jsonify(response)

@web_bp.route('/generate_secret_key')
def generate_key():    
    # La cadena que deseas usar como semilla
    seed_string = "importador2023"

    # Utiliza hashlib para derivar una clave secreta a partir de la cadena
    secret_key = hashlib.pbkdf2_hmac('sha256', seed_string.encode('utf-8'), b'salt', 100000)
    secret_key_hex = secret_key.hex()
    # print(secret_key_hex)
    return secret_key_hex

@web_bp.route('/update_user', methods=['GET', 'POST'])
def update_user_post():
    # print("OK REQUEST", request.form.get('id_user'))
    response = user_controller.update_user()
    return jsonify(response)

@web_bp.route('/delete_user', methods=['GET', 'POST'])
def delete_user_post():
    response = user_controller.delete_user()
    return jsonify(response)

