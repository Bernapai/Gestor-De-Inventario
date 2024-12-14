from flask import Blueprint, request
from controllers.proovedorController import proovedorController

proovedor_bp = Blueprint('proovedor_bp', __name__)

# Ruta para obtener todos los proveedores
@proveedor_bp.route('/proveedores', methods=['GET'])
def obtener_proveedores():
    return ProveedorController.obtener_proveedores()

# Ruta para obtener un proveedor por id
@proveedor_bp.route('/proveedor/<int:id_proveedor>', methods=['GET'])
def obtener_proveedor(id_proveedor):
    return ProveedorController.obtener_proveedor(id_proveedor)

# Ruta para agregar un nuevo proveedor
@proveedor_bp.route('/proveedor', methods=['POST'])
def agregar_proveedor():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return ProveedorController.agregar_proveedor(data)

# Ruta para actualizar un proveedor
@proveedor_bp.route('/proveedor/<int:id_proveedor>', methods=['PUT'])
def actualizar_proveedor(id_proveedor):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return ProveedorController.actualizar_proveedor(id_proveedor, data)

# Ruta para eliminar un proveedor
@proveedor_bp.route('/proveedor/<int:id_proveedor>', methods=['DELETE'])
def eliminar_proveedor(id_proveedor):
    return ProveedorController.eliminar_proveedor(id_proveedor)