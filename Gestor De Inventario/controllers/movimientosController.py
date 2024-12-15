from flask import jsonify
from models.services.movimientosServices import movimientosServices

class movimientosController:
     @staticmethod
    def agregar_movimiento():
        try:
            data = request.get_json()
            # Validación básica de los datos
            if not data or 'id_producto' not in data or 'cantidad' not in data or 'tipo_movimiento' not in data or 'usuario' not in data:
                return jsonify({'error': 'Datos incompletos'}), 400
            
            # Llamar al servicio para agregar el movimiento
            nuevo_movimiento = movimientoServices.agregar_movimiento(
                data['id_producto'], 
                data['cantidad'], 
                data['tipo_movimiento'], 
                data['usuario']
            )
            return jsonify(nuevo_movimiento.serialize()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def obtener_todos_movimientos():
        try:
            # Llamar al servicio para obtener todos los movimientos
            movimientos = movimientoServices.obtener_todos_movimientos()
            # Retornar los movimientos serializados
            return jsonify([movimiento.serialize() for movimiento in movimientos]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def obtener_movimiento_por_id(id_movimiento):
        try:
            # Llamar al servicio para obtener el movimiento por ID
            movimiento = movimientoServices.obtener_movimiento_por_id(id_movimiento)
            if movimiento:
                return jsonify(movimiento.serialize()), 200
            else:
                return jsonify({'error': 'Movimiento no encontrado'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def actualizar_movimiento(id_movimiento):
        try:
            data = request.get_json()
            # Validación de datos
            if not data:
                return jsonify({'error': 'Datos incompletos'}), 400
            
            # Llamar al servicio para actualizar el movimiento
            movimiento_actualizado = movimientoServices.actualizar_movimiento(
                id_movimiento,
                data.get('cantidad'),
                data.get('tipo_movimiento'),
                data.get('usuario')
            )
            
            return jsonify(movimiento_actualizado.serialize()), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def eliminar_movimiento(id_movimiento):
        try:
            # Llamar al servicio para eliminar el movimiento
            movimientoServices.eliminar_movimiento(id_movimiento)
            return jsonify({'message': 'Movimiento eliminado correctamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
