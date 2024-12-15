from flask import blueprint, request
from controllers.ventasController import ventasController

# Creamos un Blueprint para las rutas de ventas
venta_bp = Blueprint('venta_bp', __name__)

# Ruta para obtener todas las ventas
@venta_bp.route('/ventas', methods=['GET'])
def obtener_ventas():
    return VentaController.obtener_ventas()

# Ruta para obtener una venta por id
@venta_bp.route('/venta/<int:id_venta>', methods=['GET'])
def obtener_venta(id_venta):
    return VentaController.obtener_venta(id_venta)

# Ruta para agregar una nueva venta
@venta_bp.route('/venta', methods=['POST'])
def agregar_venta():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return VentaController.agregar_venta(data)

# Ruta para actualizar una venta existente
@venta_bp.route('/venta/<int:id_venta>', methods=['PUT'])
def actualizar_venta(id_venta):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return VentaController.actualizar_venta(id_venta, data)

# Ruta para eliminar una venta
@venta_bp.route('/venta/<int:id_venta>', methods=['DELETE'])
def eliminar_venta(id_venta):
    return VentaController.eliminar_venta(id_venta)