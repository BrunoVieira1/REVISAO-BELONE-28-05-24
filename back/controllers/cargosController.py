from flask import request
from database.db import db
from models.cargos import Cargos

def cargo_controller():
  if request.method == 'POST':
    try:
      data = request.get_json()
      cargo = Cargos(data['nome'])
      db.session.add(cargo)
      db.session.commit()
      return 'Cargo Inserido com sucesso', 200
    except Exception as e:
      return {'error: erro ao inserir cargo. Erro: {} '.format(str(e)), 400}
  elif request.method == 'GET':
    try:
      data = Cargos.query.all()
      new = {'cargos': [cargo.to_dict() for cargo in data]}
      return new, 200
    except Exception as e:
      return {'error: erro ao pesquisar. Erro {} '.format(str(e)), 400}