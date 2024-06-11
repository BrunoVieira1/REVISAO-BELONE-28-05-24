from flask import request, render_template
from database.db import db
from models.clientes import Clientes

def clientes_controller():
        if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Clientes(data['nome'], data['email'], data['cargo_id'])
                db.session.add(user)
                db.session.commit()
                
                return 'Usuário criado', 200
            except Exception as e:
                return 'Usuário não criado', 405
        elif request.method == 'GET':
            try:
                data = Clientes.query.all()
                teste = {'clientes': [cliente.to_dict() for cliente in data]}
                return teste
                #return render_template('clientes.html', data={'clientes': [cliente.to_dict() for cliente in data]})
            except Exception as e:
                return 'Usuários não foram buscados', 405
        elif request.method == 'PUT':
            try:
                data = request.get_json()
                put_cliente_id = data['id']
                put_cliente = Clientes.query.get(put_cliente_id)
                if put_cliente is None:
                    return{'error': 'cliente nao encontrado'}, 404
                put_cliente.nome = data.get('nome', put_cliente.nome)
                put_cliente.email = data.get('email', put_cliente.email)
                print(put_cliente.nome, put_cliente.email)
                db.session.commit()
                return 'Cliente atualizado', 200
            except Exception as e:
                return {'error': 'Erro ao atualizar{}'.format(e)}, 400
        elif request.method == 'DELETE':
            try:
                data = request.get_json()
                delete_cliente_id = data['id']
                delete_cliente = Clientes.query.get(delete_cliente_id)
                if delete_cliente is None:
                    return{'error': 'cliente nao encontrado'}, 404
                db.session.delete(delete_cliente)
                db.session.commit()
                return 'Cliente deletado', 200
            except Exception as e:
                return {'error': 'Erro ao atualizar{}'.format(e)}, 400
