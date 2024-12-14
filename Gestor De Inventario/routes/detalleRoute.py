from flask import Blueprint, jsonify, request
from models.entidades.detalle import Detalle

detalle_bp = Blueprint('detalle_bp', __name__)

@detalle_bp.route('/detalle', methods=['GET'])
def obtener_detalle():
    detalles = Detalle.obtener_todos()
    return jsonify([detalle.serialize() for detalle in detalles])

@detalle_bp.route('/detalle/<int:id_detalle>', methods=['GET'])
def obtener_detalle_por_id(id_detalle):
    detalle = Detalle.obtener_por_id(id_detalle)
    if detalle:
        return jsonify(detalle.serialize())
    else:
        return jsonify({'error': 'Detalle no encontrado'}), 404




@detalle_bp.route('/detalle', methods=['POST'])
def agregar_detalle():
    data = request.get_json()
    cantidad = data.get('cantidad')
    precio_unitario = data.get('precio_unitario')
    
    if not cantidad or not precio_unitario:
        return jsonify({'error': 'Faltan datos obligatorios'}), 400
    else:
        detalle = Detalle( cantidad, precio_unitario)
        detalle.agregar()
        return jsonify(detalle.serialize()), 201

@detalle_bp.route('/detalle/<int:id_detalle>', methods=['PUT'])
def actualizar_detalle(id_detalle):
    detalle = Detalle.obtener_por_id(id_detalle)
    if detalle:
        data = request.get_json()
        detalle.actualizar(
            id_producto=data.get('id_producto', detalle.id_producto),
            cantidad=data.get('cantidad', detalle.cantidad),
            precio_unitario=data.get('precio_unitario', detalle.precio_unitario)
        )
        return jsonify(detalle.serialize())
    return jsonify({'error': 'Detalle no encontrado'}), 404

@detalle_bp.route('/detalle/<int:id_detalle>', methods=['DELETE'])
def eliminar_detalle(id_detalle):
    detalle = Detalle.obtener_por_id(id_detalle)
    if detalle:
        detalle.eliminar()
        return jsonify({'message': 'Detalle eliminado'})
    return jsonify({'error': 'Detalle no encontrado'}), 404

