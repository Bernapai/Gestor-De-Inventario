# carpeta_padre/services/detalleServices.py

from entidades.detalle import Detalle, db  # Importamos el modelo Detalle

class detalleServices:

    # Método para agregar un detalle de venta
    @staticmethod
    def agregar_detalle(id_venta, id_producto, cantidad, precio_unitario):
        nuevo_detalle = Detalle(id_venta, id_producto, cantidad, precio_unitario)
        db.session.add(nuevo_detalle)
        db.session.commit()
        return nuevo_detalle
    
    # Método para actualizar un detalle de venta
    @staticmethod
    def actualizar_detalle(id_detalle, cantidad=None, precio_unitario=None):
        detalle = Detalle.query.get(id_detalle)
        if detalle:
            if cantidad:
                detalle.cantidad = cantidad
            if precio_unitario:
                detalle.precio_unitario = precio_unitario
            db.session.commit()
            return detalle
        else:
            return None  # Si no se encuentra el detalle, devolvemos None
    
    # Método para eliminar un detalle de venta
    @staticmethod
    def eliminar_detalle(id_detalle):
        detalle = Detalle.query.get(id_detalle)
        if detalle:
            db.session.delete(detalle)
            db.session.commit()
        else:
            raise ValueError(f"No se encontró el detalle con ID: {id_detalle}")
    
    # Método para obtener todos los detalles de venta
    @staticmethod
    def obtener_todos_detalles():
        return Detalle.query.all()

    # Método para obtener un detalle de venta por ID
    @staticmethod
    def obtener_detalle_por_id(id_detalle):
        return Detalle.query.get(id_detalle)
