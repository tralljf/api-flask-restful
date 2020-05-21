from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)



@auth.verify_password
def validate(login,password):
    if not (login, password):
        return False
    
    return Usuarios.query.filter_by(login=login, password=password).first()



class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()

        response = {
            "id": pessoa.id,
            "nome": pessoa.nome,
            "idade": pessoa.idade
        }

        return response
        
    @auth.login_required
    def post(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()

        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome'] 
        
        if 'idade' in dados:
            pessoa.idade = dados['idade'] 

        pessoa.save()

        response = {
            "id": pessoa.id,
            "nome": pessoa.nome,
            "idade": pessoa.idade
        }

        return response


api.add_resource(Pessoa, '/pessoas/<string:nome>')

if __name__ == '__main__':
    app.run(debug=True)