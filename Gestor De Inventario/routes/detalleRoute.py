from flask import Blueprint, request
from controllers.detalleController import detalleController

detalle_bp = Blueprint('detalle_bp', __name__)

# Ruta para obtener todos los detalles de venta
@detalle_bp.route('/detalles', methods=['GET'])
def obtener_detalles():
    return detalleController.obtener_detalles()

# Ruta para obtener un detalle por id
@detalle_bp.route('/detalle/<int:id_detalle>', methods=['GET'])
def obtener_detalle(id_detalle):
    return detalleController.obtener_detalle(id_detalle)

# Ruta para agregar un nuevo detalle
@detalle_bp.route('/detalle', methods=['POST'])
def agregar_detalle():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return detalleController.agregar_detalle(data)

# Ruta para actualizar un detalle
@detalle_bp.route('/detalle/<int:id_detalle>', methods=['PUT'])
def actualizar_detalle(id_detalle):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return detalleController.actualizar_detalle(id_detalle, data)

# Ruta para eliminar un detalle
@detalle_bp.route('/detalle/<int:id_detalle>', methods=['DELETE'])
def eliminar_detalle(id_detalle):
    return detalleController.eliminar_detalle(id_detalle)