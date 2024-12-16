from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from routes.categoriaRoute import categoria_bp
from routes.clienteRoute import cliente_bp
from routes.detalleRoute import detalle_bp
from routes.movimientosRoute import movimientos_bp
from routes.productoRoute import producto_bp
from routes.proovedorRoute import proovedor_bp
from routes.usuarioRoute import usuario_bp
from routes.ventasRoute import ventas_bp



# Crear la aplicación de Flask
app = Flask(__name__)

# Cargar la configuración desde config.py
app.config.from_object(Config)

# Instanciar SQLAlchemy y asociarlo a la aplicación
db = SQLAlchemy(app)

# Registro de Blueprints sin url_prefix
app.register_blueprint(categoria_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(detalle_bp)
app.register_blueprint(movimientos_bp)
app.register_blueprint(producto_bp)
app.register_blueprint(proovedor_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(ventas_bp)



# Definir rutas u otras configuraciones aquí

if __name__ == '__main__':
    app.run(debug=True)