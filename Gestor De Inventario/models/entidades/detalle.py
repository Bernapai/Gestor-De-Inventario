from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Detalle(db.Model):
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

   