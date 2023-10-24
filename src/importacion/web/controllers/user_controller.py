from flask import Blueprint, render_template, request, jsonify
from src.importacion.models.users import User
from src.importacion.database.connection import db


def lists():
    # Lógica para listar publicaciones
    # User.query.all()
    user = User.query.all()
    print(user)
    response = []
    
    for value in user:
        data = {
            'id_user': value.id_user,
            'first_name': value.first_name,
            'last_name': value.last_name,
            'age': value.age,
            'gender': value.gender
        }
        
        response.append(data)
        
    return {
        'data':response,
        'msg':'success'
    }

def create_user():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    user = User(first_name, last_name, age, gender)
    print("Registra user", user)
    

    # user = User(id_user, first_name, last_name)
    user_serializado = user.to_dict()
    print("Serializado OBJ", user_serializado)
    user.save()
    return {
        'status':'success',
        'msg': 'User created!',
        'data': {
            'user_data': user_serializado
        },
    }

def update_user():
    id_user = request.form.get('id_user')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    user = User.query.filter_by(id_user=id_user).first()
    
    
    user.first_name = first_name
    user.last_name = last_name
    user.age = age
    user.gender = gender
    # user = User(id_user, first_name, last_name)
    user_serializado = user.to_dict()
    print("Serializado OBJ", user_serializado)
    
    user.update()
    
    return {
        'status':'success',
        'msg': 'User updated!',
        'data': {
            'id_user':id_user,
            'user_data': user_serializado
        },
    }
    
    
def delete_user():
    print("DELETE",request.form.get('id_user'))
    id_user = request.form.get('id_user')
    user = User.query.filter_by(id_user=id_user).first()
    user_serializado = user.to_dict()
    
    user.delete()

    return {
        'status': 'success',
        'msg': 'User deleted!',        
        'data': {
            'id_user':id_user,
            'user_data': user_serializado
        }
    }
