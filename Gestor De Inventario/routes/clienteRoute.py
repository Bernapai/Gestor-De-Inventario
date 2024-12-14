from flask import Blueprint,  request
from controllers.clienteController import clienteController


cliente_bp = Blueprint('cliente_bp',__name__ )

# Ruta para obtener todos los clientes
@cliente_bp.route('/clientes', methods=['GET'])
def obtener_clientes():
    return clienteController.obtener_clientes()

# Ruta para obtener un cliente por id
@cliente_bp.route('/cliente/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    return clienteController.obtener_cliente(id_cliente)

# Ruta para agregar un nuevo cliente
@cliente_bp.route('/cliente', methods=['POST'])
def agregar_cliente():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return clienteController.agregar_cliente(data)

# Ruta para actualizar un cliente
@cliente_bp.route('/cliente/<int:id_cliente>', methods=['PUT'])
def actualizar_cliente(id_cliente):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return clienteController.actualizar_cliente(id_cliente, data)

# Ruta para eliminar un cliente
@cliente_bp.route('/cliente/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    return clienteController.eliminar_cliente(id_cliente)