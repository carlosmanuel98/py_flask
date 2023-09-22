from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/importacion_test'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy()
