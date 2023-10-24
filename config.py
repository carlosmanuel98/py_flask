import os

class Config:
    DEBUG = False
    SECRET_KEY = '4b8cd117b6dd5fe450d2f554201c7c397cb4de596909b2ef9f71c9110bb8f354'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///my_database.db'  # Usando una base de datos SQLite para este ejemplo
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_ECHO = True  # Esto imprime las consultas SQL en la consola para fines de depuración
    # Otras configuraciones específicas para el entorno de desarrollo
    FLASK_ENV = 'development'
class ProductionConfig(Config):
    # DEBUG = True
    
    SECRET_KEY = 'tu_clave_secreta_de_produccion'
    # Otras configuraciones específicas para el entorno de producción

# Puedes definir más configuraciones para otros entornos como pruebas, staging, etc.

# Configuración por defecto (generalmente desarrollo)
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config():
    # la variable de entorno FLASK_ENV no está definida en las variables de entorno del sistema, 
    # se utiliza 'default' como valor predeterminado.
    # environment = 'default'
    environment = os.environ.get('FLASK_ENV', 'development')
    # print(environment)
    # environment = DevelopmentConfig.FLASK_ENV
    return app_config.get(environment)




