# carpeta_padre/services/proveedorServices.py

from entidades.proveedor import Proveedor, db

class proveedorServices:

    # Método para agregar un nuevo proveedor
    @staticmethod
    def agregar_proveedor(nombre, telefono, email, direccion=None):
        nuevo_proveedor = Proveedor(nombre, telefono, email, direccion)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return nuevo_proveedor  

    # Método para actualizar un proveedor
    @staticmethod
    def actualizar_proveedor(id_proveedor, nombre=None, telefono=None, email=None, direccion=None):
        proveedor = Proveedor.query.get(id_proveedor)
        if proveedor:
            if nombre:
                proveedor.nombre = nombre
            if telefono:
                proveedor.telefono = telefono
            if email:
                proveedor.email = email
            if direccion:
                proveedor.direccion = direccion
            db.session.commit()
            return proveedor  
        else:
            return None  # Si no se encuentra el proveedor, devolvemos None

    # Método para eliminar un proveedor
    @staticmethod
    def eliminar_proveedor(id_proveedor):
        proveedor = Proveedor.query.get(id_proveedor)
        if proveedor:
            db.session.delete(proveedor)
            db.session.commit()
        else:
            raise ValueError(f"No se encontró el proveedor con ID: {id_proveedor}")

    # Método para obtener todos los proveedores
    @staticmethod
    def obtener_todos_proveedores():
        return Proveedor.query.all()  

    # Método para obtener un proveedor por ID
    @staticmethod
    def obtener_proveedor_por_id(id_proveedor):
        return Proveedor.query.get(id_proveedor) 

    # Método para obtener un proveedor por nombre
    @staticmethod
    def obtener_proveedor_por_nombre(nombre):
        return Proveedor.query.filter_by(nombre=nombre).first()  
