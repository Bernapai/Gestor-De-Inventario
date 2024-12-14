from flask import Blueprint,  request
from controllers.usuarioController import usuarioController

# Creamos un Blueprint para las rutas de usuario

usuario_bp = Blueprint('usuario_bp', __name__)


# Ruta para obtener todos los usuarios
@usuario_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return UsuarioController.obtener_usuarios()

# Ruta para obtener un usuario por id
@usuario_bp.route('/usuario/<int:id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    return UsuarioController.obtener_usuario(id_usuario)

# Ruta para agregar un nuevo usuario
@usuario_bp.route('/usuario', methods=['POST'])
def agregar_usuario():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return UsuarioController.agregar_usuario(data)

# Ruta para actualizar un usuario
@usuario_bp.route('/usuario/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return UsuarioController.actualizar_usuario(id_usuario, data)

# Ruta para eliminar un usuario
@usuario_bp.route('/usuario/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    return UsuarioController.eliminar_usuario(id_usuario)