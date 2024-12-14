# carpeta_padre/services/usuarioServices.py

from entidades.usuario import Usuario, db

class usuarioServices:

    # Método para agregar un nuevo usuario
    @staticmethod
    def agregar_usuario(nombre_usuario, contraseña, rol):
        nuevo_usuario = Usuario(nombre_usuario, contraseña, rol)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario  

    # Método para actualizar un usuario
    @staticmethod
    def actualizar_usuario(id_usuario, nombre_usuario=None, contraseña=None, rol=None):
        usuario = Usuario.query.get(id_usuario)
        if usuario:
            if nombre_usuario:
                usuario.nombre_usuario = nombre_usuario
            if contraseña:
                usuario.contraseña = contraseña
            if rol:
                usuario.rol = rol
            db.session.commit()
            return usuario  
        else:
            return None  # Si no se encuentra el usuario, devolvemos None

    # Método para eliminar un usuario
    @staticmethod
    def eliminar_usuario(id_usuario):
        usuario = Usuario.query.get(id_usuario)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
        else:
            raise ValueError(f"No se encontró el usuario con ID: {id_usuario}")

    # Método para obtener todos los usuarios
    @staticmethod
    def obtener_todos_usuarios():
        return Usuario.query.all()  

    # Método para obtener un usuario por ID
    @staticmethod
    def obtener_usuario_por_id(id_usuario):
        return Usuario.query.get(id_usuario) 

    # Método para obtener un usuario por nombre de usuario
    @staticmethod
    def obtener_usuario_por_nombre(nombre_usuario):
        return Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()  
