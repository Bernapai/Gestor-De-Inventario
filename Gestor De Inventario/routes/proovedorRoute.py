from flask import Blueprint, jsonify, request
from models.entidades.proovedor import Proovedor

proovedor_bp = Blueprint('proovedor_bp', __name__)

@proovedor_bp.route('/proveedores', methods=['GET'])
def obtener_proveedores():
    proveedores = Proovedor.obtener_todos()
    return jsonify([proveedor.serialize() for proveedor in proveedores])

@proovedor_bp.route('/proveedor/<int:id_proveedor>', methods=['GET'])
def obtener_proveedor(id_proveedor):
    proveedor = Proovedor.obtener_por_id(id_proveedor)
    if proveedor:
        return jsonify(proveedor.serialize())
    else:
        return jsonify({'error': 'Proveedor no encontrado'}), 404

@proovedor_bp.route('/proveedor', methods=['POST'])
def agregar_proveedor():
    data = request.get_json()
    nombre = data.get('nombre')
    direccion = data.get('direccion')
    telefono = data.get('telefono')
    email = data.get('email')

    if not nombre or not direccion or not telefono or not email:
        return jsonify({'error': 'Faltan datos'}), 400
    else:
        proveedor = Proovedor(nombre, direccion, telefono, email)
        proveedor.agregar()
        return jsonify(proveedor.serialize()), 201

@proovedor_bp.route('/proveedor/<int:id_proveedor>', methods=['PUT'])
def actualizar_proveedor(id_proveedor):
    proveedor = Proovedor.obtener_por_id(id_proveedor)
    if proveedor:
        data = request.get_json()
        proveedor.actualizar(
            nombre=data.get('nombre', proveedor.nombre),
            direccion=data.get('direccion', proveedor.direccion),
            telefono=data.get('telefono', proveedor.telefono),
            email=data.get('email', proveedor.email)
        )
        return jsonify(proveedor.serialize())
    return jsonify({'error': 'proveedor no encontrado'}), 404

@proovedor_bp.route('/proveedor/<int:id_proveedor>', methods=['DELETE'])
def eliminar_proveedor(id_proveedor):
    proveedor = Proovedor.obtener_por_id(id_proveedor)
    if proveedor:
        proveedor.eliminar()
        return jsonify({'message': 'Proveedor eliminado'})
    return jsonify({'error': 'proveedor no encontrado'}), 404