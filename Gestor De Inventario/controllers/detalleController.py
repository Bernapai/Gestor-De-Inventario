from flask import jsonify
from models.services.detalleServices import detalleServices

class detalleController:
    @staticmethod
    def agregar_detalle():
        try:
            data = request.get_json()  # Recibir los datos del cuerpo de la solicitud

            # Validación básica de los datos
            if not data or 'id_venta' not in data or 'id_producto' not in data or 'cantidad' not in data or 'precio_unitario' not in data:
                return jsonify({'error': 'Datos incompletos'}), 400

            # Llamar al servicio para agregar el detalle
            nuevo_detalle = DetalleServices.agregar_detalle(
                data['id_venta'],        # Extraer cada campo de la data
                data['id_producto'],
                data['cantidad'],
                data['precio_unitario']
            )

            return jsonify(nuevo_detalle.serialize()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def actualizar_detalle(id_detalle, data):
        # Recibimos los datos de la solicitud y pasamos a los servicios para actualizar el detalle
        cantidad = data.get('cantidad')
        precio_unitario = data.get('precio_unitario')

        # Llamamos al servicio para actualizar el detalle
        detalle = DetalleServices.actualizar_detalle(id_detalle, cantidad, precio_unitario)
        
        if detalle is None:
            return jsonify({'mensaje': 'Detalle no encontrado'}), 404
        
        # Retornamos la respuesta serializada
        return jsonify(detalle.serialize()), 200

    @staticmethod
    def eliminar_detalle(id_detalle):
        # Llamamos al servicio para eliminar el detalle
        try:
            DetalleServices.eliminar_detalle(id_detalle)
            return jsonify({'mensaje': 'Detalle eliminado exitosamente'}), 200
        except ValueError:
            return jsonify({'mensaje': 'Detalle no encontrado'}), 404

    @staticmethod
    def obtener_todos_detalles():
        # Llamamos al servicio para obtener todos los detalles
        detalles = DetalleServices.obtener_todos_detalles()
        return jsonify([detalle.serialize() for detalle in detalles]), 200

    @staticmethod
    def obtener_detalle_por_id(id_detalle):
        # Llamamos al servicio para obtener un detalle por ID
        detalle = DetalleServices.obtener_detalle_por_id(id_detalle)
        if detalle is None:
            return jsonify({'mensaje': 'Detalle no encontrado'}), 404
        return jsonify(detalle.serialize()), 200

    @staticmethod
    def obtener_detalles_por_venta(id_venta):
        # Llamamos al servicio para obtener los detalles de una venta por ID de venta
        detalles = DetalleServices.obtener_detalles_por_venta(id_venta)
        return jsonify([detalle.serialize() for detalle in detalles]), 200

    @staticmethod
    def obtener_detalles_por_producto(id_producto):
        # Llamamos al servicio para obtener los detalles de un producto por ID de producto
        detalles = DetalleServices.obtener_detalles_por_producto(id_producto)
        return jsonify([detalle.serialize() for detalle in detalles]), 200