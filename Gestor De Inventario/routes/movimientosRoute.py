from flask import Blueprint,  request
from controllers.movimientosController import movimientosController

movimientos_bp = Blueprint('movimientos_bp', __name__)

# Ruta para obtener todos los movimientos
@movimiento_bp.route('/movimientos', methods=['GET'])
def obtener_movimientos():
    return movimientoController.obtener_movimientos()

# Ruta para obtener un movimiento por id
@movimiento_bp.route('/movimiento/<int:id_movimiento>', methods=['GET'])
def obtener_movimiento(id_movimiento):
    return movimientoController.obtener_movimiento(id_movimiento)

# Ruta para agregar un nuevo movimiento
@movimiento_bp.route('/movimiento', methods=['POST'])
def agregar_movimiento():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return movimientoController.agregar_movimiento(data)

# Ruta para actualizar un movimiento
@movimiento_bp.route('/movimiento/<int:id_movimiento>', methods=['PUT'])
def actualizar_movimiento(id_movimiento):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return movimientoController.actualizar_movimiento(id_movimiento, data)

# Ruta para eliminar un movimiento
@movimiento_bp.route('/movimiento/<int:id_movimiento>', methods=['DELETE'])
def eliminar_movimiento(id_movimiento):
    return movimientoController.eliminar_movimiento(id_movimiento)