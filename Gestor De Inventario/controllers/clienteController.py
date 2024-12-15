from flask import jsonify
from models.services.clienteServices import clienteServices


class clienteController:
    
    @staticmethod
    def agregar_cliente():
        # Recibimos los datos de la solicitud y pasamos a los servicios para agregar el cliente
        nombre = data.get('nombre')
        telefono = data.get('telefono')
        email = data.get('email')
        direccion = data.get('direccion')

        # Llamamos al servicio para agregar el cliente
        nuevo_cliente = clienteServices.agregar_cliente(nombre, telefono, email, direccion)
        
        # Retornamos la respuesta serializada
        return jsonify(nuevo_cliente.serialize()), 201

    @staticmethod
    def actualizar_cliente(id_cliente, data):
        # Recibimos los datos de la solicitud y pasamos a los servicios para actualizar el cliente
        nombre = data.get('nombre')
        telefono = data.get('telefono')
        email = data.get('email')
        direccion = data.get('direccion')

        # Llamamos al servicio para actualizar el cliente
        cliente = clienteServices.actualizar_cliente(id_cliente, nombre, telefono, email, direccion)
        
        if cliente is None:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404
        
        # Retornamos la respuesta serializada
        return jsonify(cliente.serialize()), 200

    @staticmethod
    def eliminar_cliente(id_cliente):
        # Llamamos al servicio para eliminar el cliente
        try:
            clienteServices.eliminar_cliente(id_cliente)
            return jsonify({'mensaje': 'Cliente eliminado exitosamente'}), 200
        except ValueError:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404

    @staticmethod
    def obtener_todos_clientes():
        # Llamamos al servicio para obtener todos los clientes
        clientes = clienteServices.obtener_todos_clientes()
        return jsonify([cliente.serialize() for cliente in clientes]), 200

    @staticmethod
    def obtener_cliente_por_id(id_cliente):
        # Llamamos al servicio para obtener un cliente por ID
        cliente = clienteServices.obtener_cliente_por_id(id_cliente)
        if cliente is None:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404
        return jsonify(cliente.serialize()), 200

    @staticmethod
    def obtener_cliente_por_telefono(telefono):
        # Llamamos al servicio para obtener un cliente por teléfono
        cliente = clienteServices.obtener_cliente_por_telefono(telefono)
        if cliente is None:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404
        return jsonify(cliente.serialize()), 200
    
    @staticmethod
    def obtener_cliente_por_email(email):
        # Llamamos al servicio para obtener un cliente por email
        cliente = clienteServices.obtener_cliente_por_email(email)
        if cliente is None:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404
        return jsonify(cliente.serialize()), 200

    @staticmethod
    def obtener_cliente_por_direccion(direccion):
        # Llamamos al servicio para obtener un cliente por dirección
        cliente = clienteServices.obtener_cliente_por_direccion(direccion)
        if cliente is None:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404
        return jsonify(cliente.serialize()), 200

    @staticmethod
    def buscar_cliente_por_nombre(nombre):
        # Llamamos al servicio para obtener los clientes que coinciden con el nombre
        clientes = clienteServices.buscar_cliente_por_nombre(nombre)
        if not clientes:
            return jsonify({'mensaje': 'No se encontraron clientes con ese nombre'}), 404
        return jsonify([cliente.serialize() for cliente in clientes]), 200