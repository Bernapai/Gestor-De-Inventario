# carpeta_padre/services/movimientoServices.py

from entidades.movimiento import Movimiento, db, TipoMovimiento

class movimientoServices:

    # Método para agregar un nuevo movimiento
    @staticmethod
    def agregar_movimiento(id_producto, cantidad, tipo_movimiento, usuario):
        nuevo_movimiento = Movimiento(id_producto, cantidad, tipo_movimiento, usuario)
        db.session.add(nuevo_movimiento)
        db.session.commit()
        return nuevo_movimiento  

    # Método para actualizar un movimiento
    @staticmethod
    def actualizar_movimiento(id_movimiento, cantidad=None, tipo_movimiento=None, usuario=None):
        movimiento = Movimiento.query.get(id_movimiento)
        if movimiento:
            if cantidad:
                movimiento.cantidad = cantidad
            if tipo_movimiento:
                movimiento.tipo_movimiento = tipo_movimiento
            if usuario:
                movimiento.usuario = usuario
            db.session.commit()
            return movimiento   No serializamos aquí
        else:
            return None  # Si no se encuentra el movimiento, devolvemos None

    # Método para eliminar un movimiento
    @staticmethod
    def eliminar_movimiento(id_movimiento):
        movimiento = Movimiento.query.get(id_movimiento)
        if movimiento:
            db.session.delete(movimiento)
            db.session.commit()
        else:
            raise ValueError(f"No se encontró el movimiento con ID: {id_movimiento}")

    # Método para obtener todos los movimientos
    @staticmethod
    def obtener_todos_movimientos():
        return Movimiento.query.all()  

    # Método para obtener un movimiento por ID de producto
    @staticmethod
    def obtener_movimientos_por_id_producto(id_producto):
        return Movimiento.query.filter_by(id_producto=id_producto).all()  

    # Método para obtener movimientos por fecha
    @staticmethod
    def obtener_movimientos_por_fecha(fecha):
        return Movimiento.query.filter_by(fecha=fecha).all()  

    # Método para obtener movimientos por usuario
    @staticmethod
    def obtener_movimientos_por_usuario(usuario):
        return Movimiento.query.filter_by(usuario=usuario).all()  
