from flask import Blueprint, jsonify, request
from models.entidades.usuario import Usuario

# Creamos un Blueprint para las rutas de usuario

usuario_bp = Blueprint('usuario_bp', __name__)




@usuario_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.obtener_todos()
    return jsonify([usuario.serialize() for usuario in usuarios])




@usuario_bp.route('/usuario/<int:id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    usuario = Usuario.obtener_por_id(id_usuario)
    if usuario:
        return jsonify(usuario.serialize())


@usuario_bp.route('/usuarios', methods=['POST'])
def agregar_usuario():
    data = request.get_json()
    nombre_usuario = data.get('nombre_usuario')
    contraseña = data.get('contraseña')
    rol=data.get('rol')
    fecha_creacion = data.get('fecha_creacion')

    if not nombre_usuario or not contraseña or not rol or not fecha_creacion:
        return jsonify({'error': 'Faltan datos'}), 400
    else:
        usuario = Usuario(nombre_usuario, contraseña, rol, fecha_creacion)
        usuario.agregar()
        return jsonify(usuario.serialize())



@usuario_bp.route('/usuario/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    usuario = Usuario.obtener_por_id(id_usuario)
    if usuario:
        data = request.get_json()
        nombre_usuario = data.get('nombre_usuario', usuario.nombre_usuario)
        contraseña = data.get('contraseña', usuario.contraseña)
        rol = data.get('rol', usuario.rol)
        fecha_creacion = data.get('fecha_creacion', usuario.fecha_creacion)
        
        if not nombre_usuario or not contraseña or not rol or not fecha_creacion:
            return jsonify({'error': 'Faltan datos'}), 400
        else:
            usuario.actualizar(nombre_usuario, contraseña, rol, fecha_creacion)
            return jsonify(usuario.serialize())

@usuario_bp.route('/usuario/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    usuario = Usuario.obtener_por_id(id_usuario)
    if usuario:
        usuario.eliminar()
        return jsonify({'message': 'Usuario eliminado'})
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404