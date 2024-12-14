from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definir el Enum para tipo_movimiento
class TipoMovimiento(Enum):
    ENTRADA = 'entrada'
    SALIDA = 'salida'

class Movimiento(db.Model):
    __tablename__ = 'movimientos'
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey (productos.id))
    cantidad=db.Column(db.Integer, nullable=False)
    tipo_movimiento = db.Column(Enum(TipoMovimiento), nullable=False)
    fecha = db.Column(db.Date, nullable=False, default=datetime.date.today) 
    usuario = db.Column(db.String(100), nullable=False)



    def __init__(self, id_producto, cantidad, tipo_movimiento, usuario):
        self.__id_producto = id_producto
        self.__cantidad = cantidad
        self.__tipo_movimiento = tipo_movimiento
        self.__usuario = usuario

    def serialize(self):
        return {
            'id': self.id,
            'id_producto': self.id_producto,
            'cantidad': self.cantidad,
            'tipo_movimiento': self.tipo_movimiento.name,
            'fecha': self.fecha.strftime('%Y-%m-%d'),
            'usuario': self.usuario
        }


   