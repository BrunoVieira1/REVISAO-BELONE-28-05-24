from controllers.cargosController import cargo_controller

def cargos(app):
  app.route('/cargos', methods=['POST', 'GET'])(cargo_controller)