from controllers.clientesController import clientes_controller

def clientes(app):
  app.route('/clientes', methods=['POST', 'GET', 'PUT', 'DELETE'])(clientes_controller)