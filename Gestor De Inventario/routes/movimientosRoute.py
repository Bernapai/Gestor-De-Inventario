from flask import Blueprint, jsonify, request
from models.entidades.movimientos import Movimientos

movimientos_bp = Blueprint('movimientos_bp', __name__)

@movimientos_bp.route('/movimientos', methods=['GET'])
def obtener_movimientos():
    movimientos = Movimientos.obtener_todos()
    return jsonify([movimiento.serialize() for movimiento in movimientos])

@movimientos_bp.route('/movimiento/<int:id_movimiento>', methods=['GET'])
def obtener_movimiento_por_id(id_movimiento):
    movimiento = Movimientos.obtener_por_id(id_movimiento)
    if movimiento:
        return jsonify(movimiento.serialize())
    else:
        return jsonify({'error': 'Movimiento no encontrado'}), 404


@movimientos_bp.route('/movimiento/<date:fecha>', methods=['GET'])
def obtener_movimiento_por_fecha(fecha):
    movimiento = Movimientos.obtener_por_fecha(fecha)
    if movimiento:
        return jsonify(movimiento.serialize())
    else:
        return jsonify({'error': 'Movimiento no encontrado'}), 404

@movimientos_bp.route('/movimiento/<string:usuario>', methods=['GET'])
def obtener_movimiento_por_usuario(usuario):
    movimiento=Movimientos.obtener_movimiento_por_usuario(usuario)
    if movimiento:
        return jsonify(movimiento.serialize())
    else:
        return jsonify({'error': 'Movimiento no encontrado'}), 404
        
 

@movimientos_bp.route('/movimiento', methods=['POST'])
def agregar_movimiento():
    data = request.get_json()
    fecha = data.get('fecha')
    tipo_movimiento = data.get('tipo_movimiento')
    cantidad = data.get('cantidad')
    usuario = data.get('usuario')
    
    movimiento = Movimientos(fecha, tipo_movimiento, cantidad, usuario)
    movimiento.agregar()
    return jsonify(movimiento.serialize()), 201


@movimientos_bp.route('/movimiento/<int:id_movimiento>', methods=['PUT'])
def actualizar_movimiento(id_movimiento):
    movimiento = Movimientos.obtener_por_id(id_movimiento)
    if movimiento:
        data = request.get_json()
        movimiento.actualizar(
            fecha=data.get('fecha', movimiento.fecha),
            tipo_movimiento=data.get('tipo_movimiento', movimiento.tipo_movimiento),
            cantidad=data.get('cantidad', movimiento.cantidad),
            usuario=data.get('usuario', movimiento.usuario)


@movimientos_bp.route('/movimiento/<int:id_movimiento>', methods=['DELETE'])
def eliminar_movimiento(id_movimiento):
    movimiento = Movimientos.obtener_por_id(id_movimiento)
    if movimiento:
        movimiento.eliminar()
        return jsonify({'message': 'Movimiento eliminado'})
    else:
        return jsonify({'error': 'Movimiento no encontrado'}), 404



