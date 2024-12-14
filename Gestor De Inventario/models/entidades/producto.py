from flask_sqlalchemy import SQLAlchemy

# Inicializamos la base de datos
db = SQLAlchemy()


class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock_actual = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=True)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=True)
    fecha_creacion =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)


    def __init__(self, nombre, descripcion, precio, stock_actual, categoria_id, proveedor_id=):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock_actual = stock_actual
        self.categoria_id = categoria_id
        self.proveedor_id = proveedor_id

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock_actual': self.stock_actual,
            'categoria_id': self.categoria_id,
            'proveedor_id': self.proveedor_id,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion
        }

    def actualizar(self, nombre=None, descripcion=None, precio=None, stock_actual=None, categoria_id=None, proveedor_id=None):
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if precio:
            self.precio = precio
        if stock_actual:
            self.stock_actual = stock_actual
        if categoria_id:
            self.categoria_id = categoria_id
        if proveedor_id:
            self.proveedor_id = proveedor_id
        db.session.commit()

    def eliminar(self):
        if isinstance (self,Producto):
            db.session.delete(self)
            db.session.commit()
        else:
            raise ValueError('El objeto no es de la clase Producto')

    def agregar(self):
        if isinstance (self,Producto):
            db.session.add(self)
            db.session.commit()
        else:
            raise ValueError('El objeto no es de la clase Producto')

    @classmethod
    def obtener_todos(cls):
        return cls.query.all()

    @classmethod
    def obtener_por_id(cls, id_producto):
        return cls.query.get(id_producto)

    @classmethod
    def obtener_por_nombre(cls, nombre):
        return cls.query.filter_by(nombre=nombre).first()

    