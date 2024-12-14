from flask import Blueprint, request
from controllers.productoController import productoController

# Creamos un Blueprint para las rutas de productos

producto_bp = Blueprint('producto_bp', __name__)

# Ruta para obtener todos los productos
@producto_bp.route('/productos', methods=['GET'])
def obtener_productos():
    return ProductoController.obtener_productos()

# Ruta para obtener un producto por id
@producto_bp.route('/producto/<int:id_producto>', methods=['GET'])
def obtener_producto(id_producto):
    return ProductoController.obtener_producto(id_producto)

# Ruta para agregar un nuevo producto
@producto_bp.route('/producto', methods=['POST'])
def agregar_producto():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return ProductoController.agregar_producto(data)

# Ruta para actualizar un producto
@producto_bp.route('/producto/<int:id_producto>', methods=['PUT'])
def actualizar_producto(id_producto):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return ProductoController.actualizar_producto(id_producto, data)

# Ruta para eliminar un producto
@producto_bp.route('/producto/<int:id_producto>', methods=['DELETE'])
def eliminar_producto(id_producto):
    return ProductoController.eliminar_producto(id_producto)