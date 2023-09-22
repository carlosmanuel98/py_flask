# run.py

from src import app
# from centralizador.importacion.database.connection import db
# with app.app_context():
#     db.init_app(app)
    #db.create_all()

if __name__ == '__main__':
    app.run(debug=True)#Para recargar cuando se haga cambios.
