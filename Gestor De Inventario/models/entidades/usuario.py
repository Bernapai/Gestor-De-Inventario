from flask_sqlalchemy import SQLAlchemy

# Inicializamos la base de datos
db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(100), nullable=False)
    contraseña = db.Column(db.String (255), nullable=False)
    rol=db.Column(db.String(255), nullable=False)
    fecha_creacion= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, nombre_usuario, contraseña, rol):
        self.__nombre_usuario = nombre_usuario
        self.__contraseña = contraseña
        self.__rol = rol

    
    def serialize(self):
        return {
            'id': self.id,
            'nombre_usuario': self.nombre_usuario,
            'contraseña': self.contraseña,
            'rol': self.rol,
            'fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')
        }

    def actualizar(self, nombre_usuario=None, contraseña=None, rol=None):
        if nombre_usuario:
            self.nombre_usuario = nombre_usuario
        if contraseña:
            self.contraseña = contraseña
        if rol:
            self.rol = rol
        db.session.commit()

    def eliminar(self):
        if isinstance(self, Usuario):
            db.session.delete(self)
            db.session.commit()
        else:
            raise ValueError("Este objeto no es una instancia de Usuario.")

    def agregar(self):
        if isinstance(self, Usuario):
            db.session.add(self)
            db.session.commit()
        else:
            raise ValueError("Este objeto no es una instancia de Usuario.")
    
    @classmethod
    def obtener_todos(cls):
        return cls.query.all()
    
    @classmethod
    def obtener_por_id(cls, id):
        return cls.query.get(id)
