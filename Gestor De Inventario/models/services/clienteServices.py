# carpeta_padre/services/clienteServices.py

from entidades.cliente import Cliente, db  # Importamos el modelo Cliente

class clienteServices:

    # Método para agregar un cliente
    @staticmethod
    def agregar_cliente(nombre, telefono, email, direccion=None):
        nuevo_cliente = Cliente(nombre, telefono, email, direccion)
        db.session.add(nuevo_cliente)
        db.session.commit()
        return nuevo_cliente
    
    # Método para actualizar un cliente
    @staticmethod
    def actualizar_cliente(id_cliente, telefono=None, direccion=None, email=None):
        cliente = Cliente.query.get(id_cliente)
        if cliente:
            if telefono:
                cliente.telefono = telefono
            if direccion:
                cliente.direccion = direccion
            if email:
                cliente.email = email
            db.session.commit()
            return cliente
        else:
            return None  # Si no se encuentra el cliente, devolvemos None
    
    # Método para eliminar un cliente
    @staticmethod
    def eliminar_cliente(id_cliente):
        cliente = Cliente.query.get(id_cliente)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
        else:
            raise ValueError(f"No se encontró el cliente con ID: {id_cliente}")
    
    # Método para obtener todos los clientes
    @staticmethod
    def obtener_todos_clientes():
        return Cliente.query.all()

    # Método para obtener un cliente por ID
    @staticmethod
    def obtener_cliente_por_id(id_cliente):
        return Cliente.query.get(id_cliente)

    # Método para obtener un cliente por teléfono
    @staticmethod
    def obtener_cliente_por_telefono(telefono):
        return Cliente.query.filter_by(telefono=telefono).first()
    
    # Método para obtener un cliente por email
    @staticmethod
    def obtener_cliente_por_email(email):
        return Cliente.query.filter_by(email=email).first()

    # Método para obtener un cliente por dirección
    @staticmethod
    def obtener_cliente_por_direccion(direccion):
        return Cliente.query.filter_by(direccion=direccion).first()

    # Método para buscar clientes por nombre
    @staticmethod
    def buscar_cliente_por_nombre(nombre):
        return Cliente.query.filter(Cliente.nombre.ilike(f'%{nombre}%')).all()
