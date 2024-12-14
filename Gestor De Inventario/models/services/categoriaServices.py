

from entidades.categoria import Categoria, db  

class categoriaServices:
    # Método para agregar una categoría
    @staticmethod
    def agregar_categoria(nombre, descripcion=None):
        nueva_categoria = Categoria(nombre, descripcion)
        db.session.add(nueva_categoria)
        db.session.commit()
    
    # Método para actualizar una categoría
    @staticmethod
    def actualizar_categoria(id_categoria, nombre=None, descripcion=None):
        # Obtener la categoría por ID
        categoria = Categoria.query.get(id_categoria)
        if categoria:
            # Si el nombre es proporcionado, actualizamos el nombre
            if nombre:
                categoria.nombre = nombre
            # Si la descripción es proporcionada, actualizamos la descripción
            if descripcion:
                categoria.descripcion = descripcion
            # Confirmamos los cambios en la base de datos
            db.session.commit()
        else:
            # Si no se encuentra la categoría, podemos lanzar un error o devolver None
            return None
    
    # Método para eliminar una categoría
    @staticmethod
    def eliminar_categoria(id_categoria):
        categoria = Categoria.query.get(id_categoria)
        if categoria:
            db.session.delete(categoria)
            db.session.commit()

    # Método para obtener todas las categorías
    @staticmethod
    def obtener_todas_categorias():
        return Categoria.query.all()

    # Método para obtener una categoría por ID
    @staticmethod
    def obtener_categoria_por_id(id_categoria):
        return Categoria.query.get(id_categoria)

    # Método para obtener una categoría por nombre
    @staticmethod
    def obtener_categoria_por_nombre(nombre_categoria):
        return Categoria.query.filter_by(nombre=nombre_categoria).first()
e=nombre_categoria).first()
    
