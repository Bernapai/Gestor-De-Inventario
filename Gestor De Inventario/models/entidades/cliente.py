from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    telefono = db.Column(db.String(20),nullable=True, unique=True)
    email=db.Column(db.String(100), nullable=True, unique=True)
    direccion=db.Column(db.text, nullable=True, unique=True)


    def __init__(self,nombre,telefono,email,direccion=None):
      self.__nombre = nombre
      self.__telefono = telefono
      self.__email = email
      self.__direccion = direccion


    def serialize (self):
      return {
         'id': self.id,
         'nombre': self.nombre,
         'telefono': self.telefono,
         'email': self.email,
         'direccion': self.direccion
      }

    def actualizar(self, telefono = None, direccion = None, email = None):
      if telefono:
         self.telefono = telefono
      if direccion:
         self.direccion = direccion
      if email:
         self.email = email
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
    def obtener_por_id(cls, id_cliente):
        return cls.query.get(id_cliente)

    @classmethod
    def obtener_por_telefono(cls, telefono):
        return cls.query.filter_by(telefono=telefono).first()
    
    @classmethod
    def obtener_por_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def obtener_por_direccion(cls, direccion):
        return cls.query.filter_by(direccion=direccion).first()

    @classmethod
    def buscar_por_nombre(cls, nombre):
        return cls.query.filter(cls.nombre.ilike(f'%{nombre}%')).all()