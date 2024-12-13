from flask import Blueprint, jsonify, request
from models.entidades.cliente import Cliente


cliente_bp = Blueprint('cliente_bp',__name__ )

@cliente_bp.route('/clientes', methods=['GET'])
def obtener_clientes():
    clientes = Cliente.obtener_todos()
    return jsonify([cliente.serialize() for cliente in clientes])

@cliente_bp.route('/cliente/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    cliente = Cliente.obtener_por_id(id_cliente)
    if cliente:
        return jsonify(cliente.serialize())
    else:
        return jsonify({'error': 'Cliente no encontrado'}), 404

@cliente_bp.route('/cliente', methods=['POST'])
def agregar_cliente():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    telefono = data.get('telefono')
    direccion = data.get('direccion')

    if not nombre or not email or not telefono or not direccion:
        return jsonify({'error': 'Faltan datos'}), 400

    cliente = Cliente(nombre, apellidos, email, telefono, direccion)
    cliente.agregar()
    return jsonify(cliente.serialize())

@cliente_bp.route('/cliente/<int:id_cliente>', methods=['PUT'])
def actualizar_cliente(id_cliente):
    cliente = Cliente.obtener_por_id(id_cliente)
    if cliente:
        data = request.get_json()
        cliente.actualizar(
            nombre=data.get('nombre', cliente.nombre),
            email=data.get('email', cliente.email),
            telefono=data.get('telefono', cliente.telefono),
            direccion=data.get('direccion', cliente.direccion)
        )
        return jsonify(categoria.serialize())
    return jsonify({'error': 'cliente no encontrado'}), 404

@cliente_bp.route('/cliente/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    cliente = Cliente.obtener_por_id(id_cliente)
    if cliente:
        cliente.eliminar()
        return jsonify({'message': 'Cliente eliminado'})
    return jsonify({'error': 'Cliente no encontrado'}), 404