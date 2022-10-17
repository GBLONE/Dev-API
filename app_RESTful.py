from flask import Flask, request
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)


desenvolvedores = [
    {
        'id': 0,
        'Nome': 'Gabriel',
        'Habilidades': ['Python', 'Flask']},
    {
        'id': 1,
        'Nome': 'Rafael',
        'Habilidades': ['Python', 'Django']
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'Status': 'Error', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador da API'
            response = {'status': 'Error', 'Mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        #json.decoder.JSONDecoder()
        desenvolvedores['id'] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'Status': 'Sucesso',
                'mensagem': 'Registro excluído'})


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)
