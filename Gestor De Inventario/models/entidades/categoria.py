from flask_sqlalchemy import SQLAlchemy

# Inicializamos la base de datos
db = SQLAlchemy()


class categoria(db.Model):
    __tablename__ = 'categoria'
   # Definimos los atributos de la clase (columnas de la tabla)
    id = db.Column(db.Integer, primary_key=True)  # ID de la categoría (clave primaria)
    nombre = db.Column(db.String(100), nullable=False, unique=True)  # Nombre de la categoría
    descripcion = db.Column(db.String(255))  # Descripción de la categoría (opcional)
    


      # Constructor para inicializar la categoría
    def __init__(self, nombre, descripcion=None):
        self.__nombre = nombre
        self.__descripcion = descripcion


     # Método para representar la categoría como un diccionario (útil para las respuestas JSON)
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.__nombre,
            'descripcion': self.__descripcion
        }

     # Método para actualizar la categoría
    def actualizar(self, nombre=None, descripcion=None):
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        db.session.commit()

    # Método para eliminar la categoría
    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

    # Método para guardar la categoría en la base de datos
    def agregar(self):
        db.session.add(self)
        db.session.commit()

    # Método de clase para obtener todas las categorías
    @classmethod
    def obtener_todas(cls):
        return cls.query.all()

    # Método de clase para obtener una categoría por ID
    @classmethod
    def obtener_por_id(cls, id_categoria):
        return cls.query.get(id_categoria)

    # Método de clase para obtener una categoría por nombre
    @classmethod
    def obtener_por_nombre(cls, nombre_categoria):
        return cls.query.filter_by(nombre=nombre_categoria).first()
    
