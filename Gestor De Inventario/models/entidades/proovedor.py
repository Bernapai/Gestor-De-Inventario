from flask_sqlalchemy import SQLAlchemy

# Inicializamos la base de datos
db = SQLAlchemy()



class Proovedor(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    telefono = db.Column(db.String(20), nullable=True, unique=True)
    email = db.Column(db.String(100), nullable=True, unique=True)
    direccion = db.Column(db.text, nullable=True, unique=True)


    def __init__(self,nombre,telefono,email,direccion):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        self.__direccion = direccion

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'email': self.email,
            'direccion': self.direccion
        }

    