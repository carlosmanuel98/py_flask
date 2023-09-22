from flask import Blueprint, render_template, request, jsonify
from decouple import config#paquete para variable de entorno


mobile_bp = Blueprint('mobile_home', __name__)
@mobile_bp.route('/')
def index():
    # Lógica para listar publicaciones
    return jsonify('Bienvenido al app ---MOBILE---')

@mobile_bp.route('/list')
def listar():
    # Lógica para listar publicaciones
    return jsonify('Lista mobile')
