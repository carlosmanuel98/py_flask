from ..database.connection import db

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'sys_usuarios'
    id_user     = db.Column(db.Integer, primary_key=True)
    first_name  = db.Column(db.String, nullable=True)
    last_name   = db.Column(db.String, nullable=True)
    age         = db.Column(db.Integer, nullable=True)
    sexo        = db.Column(db.String, nullable=True)

    def __init__(self, first_name, last_name, age=None, sexo=None):
        self.first_name = first_name,
        self.last_name = last_name,
        self.age = age,
        self.sexo = sexo,
    

