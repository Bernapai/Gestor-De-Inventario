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

    def actualizar(self, nombre=None, telefono=None, email=None, direccion=None):
        if nombre:
            self.nombre = nombre
        if telefono:
            self.telefono = telefono
        if email:
            self.email = email
        if direccion:
            self.direccion = direccion

    def eliminar(self):
        if isinstance (self, Proovedor ):
            db.session.delete(self)
            db.session.commit()
        else:
            raise Exception('No se puede eliminar un objeto de una clase diferente a Proveedor')

    def agregar(self):
        if isinstance (self, Proovedor ):
            db.session.add(self)
            db.session.commit()
        else:
            raise Exception('No se puede agregar un objeto de una clase diferente a Proveedor')

    @classmethod
    def obtenerTodos(cls):
        return cls.query.all()
    
    @classmethod
    def obtener_por_id(cls, id_proveedor):
        return cls.query.get(id_proveedor)
        