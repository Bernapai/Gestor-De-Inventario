# routes/categoria_routes.py
from flask import Blueprint, jsonify, request
from app.models.categoria import Categoria

# Creamos un Blueprint para las rutas de categoria
categoria_bp = Blueprint('categoria_bp', __name__)

# Ruta para obtener todas las categorías
@categoria_bp.route('/categorias', methods=['GET'])
def obtener_categorias():
    categorias = Categoria.obtener_todas()
    return jsonify([categoria.serialize() for categoria in categorias])

# Ruta para obtener una categoría por id
@categoria_bp.route('/categoria/<int:id_categoria>', methods=['GET'])
def obtener_categoria(id_categoria):
    categoria = Categoria.obtener_por_id(id_categoria)
    if categoria:
        return jsonify(categoria.serialize())
    return jsonify({'error': 'Categoría no encontrada'}), 404

# Ruta para agregar una nueva categoría
@categoria_bp.route('/categoria', methods=['POST'])
def agregar_categoria():
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')

    if not nombre:
        return jsonify({'error': 'El nombre de la categoría es obligatorio'}), 400

    categoria = Categoria(nombre, descripcion)
    categoria.agregar()
    return jsonify(categoria.serialize()), 201

# Ruta para actualizar una categoría
@categoria_bp.route('/categoria/<int:id_categoria>', methods=['PUT'])
def actualizar_categoria(id_categoria):
    categoria = Categoria.obtener_por_id(id_categoria)
    if categoria:
        data = request.get_json()
        categoria.actualizar(
            nombre=data.get('nombre', categoria.nombre),
            descripcion=data.get('descripcion', categoria.descripcion)
        )
        return jsonify(categoria.serialize())
    return jsonify({'error': 'Categoría no encontrada'}), 404

# Ruta para eliminar una categoría
@categoria_bp.route('/categoria/<int:id_categoria>', methods=['DELETE'])
def eliminar_categoria(id_categoria):
    categoria = Categoria.obtener_por_id(id_categoria)
    if categoria:
        categoria.eliminar()
        return jsonify({'message': 'Categoría eliminada'})
    return jsonify({'error': 'Categoría no encontrada'}), 404
