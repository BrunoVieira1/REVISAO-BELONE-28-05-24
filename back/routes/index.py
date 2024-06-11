from routes.clientesRoutes import clientes
from routes.homeRoutes import home
from routes.cargosRoutes import cargos


def default_routes(app):
  clientes(app)
  home(app)
  cargos(app)