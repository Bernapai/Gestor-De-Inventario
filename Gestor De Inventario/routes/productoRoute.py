from flask import Blueprint, jsonify, request
from models.entidades.producto import Producto

# Creamos un Blueprint para las rutas de productos

producto_bp = Blueprint('producto_bp', __name__)


# Ruta para obtener todos los productos

@producto_bp.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.obtener_todos()
    return jsonify([producto.serialize() for producto in productos])


# Ruta para obtener un producto por id

@producto_bp.route('/producto/<int:id_producto>', methods=['GET'])
def obtener_producto(id_producto):
    producto = Producto.obtener_por_id(id_producto)
    if producto:
        return jsonify(producto.serialize())
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404


# Ruta para agregar un producto

@producto_bp.route('/producto', methods=['POST'])
def agregar_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    precio = data.get('precio')
    stock_actual = data.get('stock_actual')
    categoria_id = data.get('categoria_id')
    proovedor_id = data.get('proovedor_id')

    if not nombre or not descripcion or not precio or not stock_actual or not categoria_id or not proovedor_id:
        return jsonify({'error': 'Faltan datos'}), 400
    else:
        producto = Producto(nombre, descripcion, precio, stock_actual, categoria_id, proovedor_id)
        producto.agregar()
        return jsonify(producto.serialize()), 201

@producto_bp.route('/producto/<int: id_producto>', methods=['PUT'])
def actualizar_producto(id_producto):
    producto = Producto.obtener_por_id(id_producto)
    if producto:
        data = request.get_json()
        producto.actualizar(
            nombre=data.get('nombre', producto.nombre),
            descripcion=data.get('descripcion', producto.descripcion),
            precio=data.get('precio', producto.precio),
            stock_actual=data.get('stock_actual', producto.stock_actual),
            categoria_id=data.get('categoria_id', producto.categoria_id),
            proovedor_id=data.get('proovedor_id', producto.proovedor_id)
        )
        return jsonify(producto.serialize())
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404


@producto_bp.route('/producto/<int:id_producto>', methods=['DELETE'])
def eliminar_producto(id_producto):
    producto = Producto.obtener_por_id(id_producto)
    if producto:
        producto.eliminar()
        return jsonify({'message': 'Producto eliminado'})
    else:
        return jsonify({'error': 'Producto no encontrado'}), 404



