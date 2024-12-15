from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ventas (db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer, primary_key=True)
    id_cliente= db.Column(db.Integer, db.ForeignKey(clientes.id))
    fecha= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    total= db.Column(db.Float, nullable=False)
    usuario= db.Column(db.String(100), nullable=False)

    def __init__(self, id_cliente, fecha, total, usuario):
        self.__id_cliente = id_cliente
        self.__fecha = fecha
        self.__total = total
        self.__usuario = usuario

    def serialize(self):
        return {
            'id': self.id,
            'id_cliente': self.id_cliente,
            'fecha': self.fecha.isoformat(),
            'total': self.total,
            'usuario': self.usuario
        }
