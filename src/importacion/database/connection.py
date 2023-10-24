from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'mysql://root:12345@importador-mysql:3306/importacion_test'#host = name container
# SQLALCHEMY_DATABASE_URI = 'mysql://root:12345@localhost:3306/importacion_test'#host = name container
# SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost:3306/importacion_test'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy() 
# mysql://username:password@server/db