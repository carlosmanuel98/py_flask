from flask import Blueprint, render_template, request, jsonify
#from decouple import config#paquete para variable de entorno
#from centralizador import db
from ...models.users import User
# from ...database.connection import db
from ...database.connection import db


def lists():
    # Lógica para listar publicaciones
    return 'Listado de usuarios.'

def register():
    msg   = "No se creo usuario, es metodo get"
    users = ['carlos', 1234] if request.method == 'POST' else [request.form.get('first_name'), request.form.get('last_name')]#if ternario

    if request.method == 'POST':
        print("*"*100)
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        for user in users:
            if(user == first_name):
                return "El usuario ya existe. Por favor, elige otro nombre de usuario."
        
        # Crea un nuevo usuario
        new_user = {'first_name': first_name, 'last_name': last_name}
        users.append(new_user)
        
        
        ######################Intenta crear usuario############################################
        data = request.form
        print(data)
        new_user = User(first_name, last_name)
        
        print("AQUI ESTA EL NUEVO")
        # save the object into the database
        db.session.add(new_user)
        db.session.commit()
        print('INSERTADO')
        # user = User(first_name=data["first_name"], last_name=data["last_name"])
        # __create(user)

        msg = "Registro exitoso. Ahora puedes iniciar sesión."
    
    response = {
        'msg': msg,
        'users': users
    }
    return response


# def __create(user_: User) -> User:
#     print(user_)
#     print("-"*10)
#     print(User)
#    # user = user_._asdict()
#     return user_db.create(user_)
