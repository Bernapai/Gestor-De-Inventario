from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class detalle(db.Model):
    __tablename__ = 'detalle_venta'
    id = db.Column(db.Integer, primary_key=True)
    id_venta = db.Column(db.Integer, db.ForeignKey('ventas.id'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)





    def __init__(self, id_venta, id_producto, cantidad, precio_unitario):
        self.__id_venta = id_venta
        self.__id_producto = id_producto
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario

    def serialize (self):
        return {
            'id': self.id,
            'id_venta': self.id_venta,
            'id_producto': self.id_producto,
            'cantidad': self.cantidad,
            'precio_unitario': self.precio_unitario
        }

    def actualizar(self, cantidad = None, precio_unitario= None):
        if cantidad:
            self.cantidad = cantidad
        if precio_unitario:
            self.precio_unitario = precio_unitario
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

    def agregar(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def obtenerTodos(cls):
        return cls.query.all()

    @classmethod
    def obtener_por_id(cls, id_detalle):
        return cls.query.get(id_detalle)

    
