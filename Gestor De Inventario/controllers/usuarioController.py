from flask import jsonify
from models.services.usuarioServices import usuarioServices

class UsuarioController:

    @staticmethod
    def agregar_usuario():
        try:
            data = request.get_json()  # Obtener los datos del cuerpo de la solicitud

            # Validación de los campos obligatorios
            if not data or 'nombre_usuario' not in data or 'contraseña' not in data or 'rol' not in data:
                return jsonify({'error': 'Datos incompletos'}), 400

            # Llamar al servicio para agregar el nuevo usuario
            nuevo_usuario = usuarioServices.agregar_usuario(
                data['nombre_usuario'],   # Extraemos los datos correctamente
                data['contraseña'],
                data['rol']
            )

            return jsonify(nuevo_usuario.serialize()), 201  # Retornar el usuario agregado en formato JSON

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def actualizar_usuario(id_usuario):
        try:
            data = request.get_json()  # Obtener los datos del cuerpo de la solicitud

            # Validación de los campos opcionales que pueden ser actualizados
            if not data:
                return jsonify({'error': 'Datos vacíos'}), 400

            # Llamar al servicio para actualizar el usuario
            usuario_actualizado = usuarioServices.actualizar_usuario(
                id_usuario,
                data.get('nombre_usuario'),
                data.get('contraseña'),
                data.get('rol')
            )

            # Si no se encuentra el usuario, retornamos un error
            if not usuario_actualizado:
                return jsonify({'error': 'Usuario no encontrado'}), 404

            return jsonify(usuario_actualizado.serialize()), 200  # Retornar el usuario actualizado

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def eliminar_usuario(id_usuario):
        try:
            # Llamar al servicio para eliminar el usuario
            usuario_eliminado = usuarioServices.eliminar_usuario(id_usuario)

            # Si no se encuentra el usuario, retornamos un error
            if not usuario_eliminado:
                return jsonify({'error': 'Usuario no encontrado'}), 404

            return jsonify({'message': 'Usuario eliminado exitosamente'}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def obtener_usuario(id_usuario):
        try:
            # Llamar al servicio para obtener un usuario por ID
            usuario = usuarioServices.obtener_usuario(id_usuario)

            # Si no se encuentra el usuario, retornamos un error
            if not usuario:
                return jsonify({'error': 'Usuario no encontrado'}), 404

            return jsonify(usuario.serialize()), 200  # Retornar el usuario encontrado

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def obtener_todos_usuarios():
        try:
            # Llamar al servicio para obtener todos los usuarios
            usuarios = usuarioServices.obtener_todos_usuarios()

            return jsonify([usuario.serialize() for usuario in usuarios]), 200  # Retornar todos los usuarios

        except Exception as e:
            return jsonify({'error': str(e)}), 500