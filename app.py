from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': '0',
        'Nome': 'Gabriel',
        'Habilidades': ['Python', 'Flask']},
    {
        'id': 1,
        'Nome': 'Rafael',
        'Habilidades': ['Python', 'Django']}
]
tarefas =[{
        'id': 0,
        'Responsável': 'Gabriel',
        'Tarefa': 'Desenvolver método GET',
        'status': 'concluído'
    }, {
        'id': 1,
        'Responsável': 'Rafael',
        'Tarefa': 'Desenvolver método POST',
        'status': 'pendente'
    }]


# Devolve um desenvolvedor pelo ID,
# e também altera e Deleta um desevolvedor.
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'Status': 'Error', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador da API'
            response = {'status': 'Error', 'Mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedor[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status':'Sucesso',
                        'mensagem':'Registro excluído'
                        })

# Lista todos os desenvolvedores
# e permite registrar um novo desenvolvedor.
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedor():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


# EXERCICIO----------------------------------------------------------
@app.route('/dev/<int:id>/tarefa/', methods=['GET', 'DELETE', 'PUT'])
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'Status': 'Error', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador da API'
            response = {'status': 'Error', 'Mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'Status': 'Sucesso',
                        'mensagem': 'Registro excluído'})


if __name__ == '__main__':
    app.run()
