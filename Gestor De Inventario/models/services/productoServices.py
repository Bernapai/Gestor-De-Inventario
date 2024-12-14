# carpeta_padre/services/productoServices.py

from entidades.producto import Producto, db

class productoServices:

    # Método para agregar un nuevo producto
    @staticmethod
    def agregar_producto(nombre, descripcion, precio, stock_actual, categoria_id, proveedor_id=None):
        nuevo_producto = Producto(nombre, descripcion, precio, stock_actual, categoria_id, proveedor_id)
        db.session.add(nuevo_producto)
        db.session.commit()
        return nuevo_producto  

    # Método para actualizar un producto
    @staticmethod
    def actualizar_producto(id_producto, nombre=None, descripcion=None, precio=None, stock_actual=None, categoria_id=None, proveedor_id=None):
        producto = Producto.query.get(id_producto)
        if producto:
            if nombre:
                producto.nombre = nombre
            if descripcion:
                producto.descripcion = descripcion
            if precio:
                producto.precio = precio
            if stock_actual:
                producto.stock_actual = stock_actual
            if categoria_id:
                producto.categoria_id = categoria_id
            if proveedor_id:
                producto.proveedor_id = proveedor_id
            db.session.commit()
            return producto  
        else:
            return None  # Si no se encuentra el producto, devolvemos None

    # Método para eliminar un producto
    @staticmethod
    def eliminar_producto(id_producto):
        producto = Producto.query.get(id_producto)
        if producto:
            db.session.delete(producto)
            db.session.commit()
        else:
            raise ValueError(f"No se encontró el producto con ID: {id_producto}")

    # Método para obtener todos los productos
    @staticmethod
    def obtener_todos_productos():
        return Producto.query.all()  

    # Método para obtener un producto por ID
    @staticmethod
    def obtener_producto_por_id(id_producto):
        return Producto.query.get(id_producto)  
    # Método para obtener un producto por nombre
    @staticmethod
    def obtener_producto_por_nombre(nombre):
        return Producto.query.filter_by(nombre=nombre).first()  
