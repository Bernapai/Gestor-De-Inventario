from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Crear la aplicación de Flask
app = Flask(__name__)

# Cargar la configuración desde config.py
app.config.from_object(Config)

# Instanciar SQLAlchemy y asociarlo a la aplicación
db = SQLAlchemy(app)

# Importar los modelos después de instanciar SQLAlchemy
# Esto es necesario para evitar errores de referencia circular
from models.entidades.categoria import Categoria

# Definir rutas u otras configuraciones aquí

if __name__ == '__main__':
    app.run(debug=True)