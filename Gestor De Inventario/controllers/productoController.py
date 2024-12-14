from flask import jsonify
from models.services.productoServices import productoServices


class productoController:

    @staticmethod
    def agregar_producto():
        try:
            data = request.get_json()  # Obtener los datos del cuerpo de la solicitud

            # Validación de los campos obligatorios
            if not data or 'nombre' not in data or 'descripcion' not in data or 'precio' not in data or 'stock_actual' not in data or 'categoria_id' not in data:
                return jsonify({'error': 'Datos incompletos'}), 400

            # Llamar al servicio para agregar el nuevo producto
            nuevo_producto = ProductoServices.agregar_producto(
                data['nombre'],          # Extraemos los datos correctamente
                data['descripcion'],
                data['precio'],
                data['stock_actual'],
                data['categoria_id'],
                data.get('proveedor_id')  # Este es opcional
            )

            return jsonify(nuevo_producto.serialize()), 201  # Retornar el producto agregado en formato JSON

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def actualizar_producto(id_producto):
        try:
            data = request.get_json()  # Obtener los datos del cuerpo de la solicitud

            # Validación de los campos opcionales que pueden ser actualizados
            if not data:
                return jsonify({'error': 'Datos vacíos'}), 400

            # Llamar al servicio para actualizar el producto
            producto_actualizado = ProductoServices.actualizar_producto(
                id_producto,
                data.get('nombre'),
                data.get('descripcion'),
                data.get('precio'),
                data.get('stock_actual'),
                data.get('categoria_id'),
                data.get('proveedor_id')
            )

            # Si no se encuentra el producto, retornamos un error
            if not producto_actualizado:
                return jsonify({'error': 'Producto no encontrado'}), 404

            return jsonify(producto_actualizado.serialize()), 200  # Retornar el producto actualizado

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def eliminar_producto(id_producto):
        try:
            # Llamar al servicio para eliminar el producto
            producto_eliminado = ProductoServices.eliminar_producto(id_producto)

            # Si no se encuentra el producto, retornamos un error
            if not producto_eliminado:
                return jsonify({'error': 'Producto no encontrado'}), 404

            return jsonify({'message': 'Producto eliminado exitosamente'}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def obtener_producto(id_producto):
        try:
            # Llamar al servicio para obtener un producto por ID
            producto = ProductoServices.obtener_producto(id_producto)

            # Si no se encuentra el producto, retornamos un error
            if not producto:
                return jsonify({'error': 'Producto no encontrado'}), 404

            return jsonify(producto.serialize()), 200  # Retornar el producto encontrado

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def obtener_todos_productos():
        try:
            # Llamar al servicio para obtener todos los productos
            productos = ProductoServices.obtener_todos_productos()

            return jsonify([producto.serialize() for producto in productos]), 200  # Retornar todos los productos

        except Exception as e:
            return jsonify({'error': str(e)}), 500