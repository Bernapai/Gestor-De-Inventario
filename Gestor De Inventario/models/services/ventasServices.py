from entidades.ventas import Ventas,db


class ventasServices:
    # Método para agregar una nueva venta
    @staticmethod
    def agregar_venta(id_cliente, fecha, total, usuario):
        nueva_venta = Ventas(id_cliente=id_cliente, fecha=fecha, total=total, usuario=usuario)
        db.session.add(nueva_venta)
        db.session.commit()
        return nueva_venta.serialize()

    @staticmethod
    def obtener_venta_por_id(venta_id):
        venta = Ventas.query.get(venta_id)
        if not venta:
            return None
        return venta.serialize()

    @staticmethod
    def actualizar_venta(venta_id, id_cliente=None, fecha=None, total=None, usuario=None):
        venta = Ventas.query.get(venta_id)
        if not venta:
            return None

        if id_cliente:
            venta.id_cliente = id_cliente
        if fecha:
            venta.fecha = fecha
        if total:
            venta.total = total
        if usuario:
            venta.usuario = usuario

        db.session.commit()
        return venta.serialize()

    @staticmethod
    def eliminar_venta(venta_id):
        venta = Ventas.query.get(venta_id)
        if not venta:
            return False
        db.session.delete(venta)
        db.session.commit()
        return True

    @staticmethod
    def listar_ventas():
        ventas = Ventas.query.all()
        return [venta.serialize() for venta in ventas]

