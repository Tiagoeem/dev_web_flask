from flask.typing import StatusCode
from model.funcoes_simples_db import select_cliente, delete_cliente, update_cliente, insert_cliente, teste_visualizar_tabelas, select_query
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/teste_rota/<int:valor>",  )
def funcao_rota_teste(valor):
    return valor


@app.route('/cliente', methods=['GET'])
def rota_selecionar_todos_clientes():
    colunas_clientes = ['sobrenome', 'nome', 'cpf', 'id_cliente']
    # Query para visualização de todos os registros da tabela de clientes
    resp_cli, sucesso = select_query('Select * from tbl_clientes')

    if sucesso:
        # Construção de uma lista com os registros convertidos para um dicionário
        lista_dict_cli = []
        for linha in resp_cli:
            lista_dict_cli.append( dict( zip( colunas_clientes, linha) ) )

        return jsonify(lista_dict_cli), 200
    else:
        return resp_cli, 404


@app.route('/cliente/<int:id>', methods=['GET'])
def rota_select_cliente( id ):

    resp, sucesso = select_cliente(id)

    if sucesso:
        return resp, 200
    else:
        return resp, 404
    


@app.route('/cliente', methods=['POST'])
def rota_insert_cli():
    try:
        content = request.get_json()
    except:
        return {'Erro': 'Entrada não é um Json Válido'}, 400

    resp, sucesso = insert_cliente(content)
    if sucesso:
        return resp, 201
    else:
        return resp, 500


@app.route('/cliente/<int:id>', methods=['PUT'])
def rota_update_cli( id ):
    try:
        content = request.get_json()
    except:
        return {'Erro': 'Entrada não é um Json Válido'}, 400

    resp, sucesso = update_cliente(id, content)
    if sucesso:
        return resp, 200 # 202 Accepted caso a atualização ocorra asincronamente
    else:
        return resp, 500 


@app.route('/cliente/<int:id>', methods=['DELETE'])
def rota_delete_cliente( id ):

    resp, sucesso = delete_cliente(id)

    if sucesso:
        return resp, 200
    else:
        return resp, 404


# Função main para teste dos exemplos
def main():
    teste_visualizar_tabelas()

    resp = select_cliente(2)

    #resp = insert_cliente({'sobrenome':'Soares', 'primeiro_nome':'Rosana', 'cpf':'999.999.999-99'})

    #resp = update_cliente(3, {'sobrenome':'do Amaral', 'primeiro_nome':'Tarsila', 'cpf':'999.999.999-99'})

    #resp = delete_cliente(3)

    print(resp)



if __name__ == '__main__':
    app.run()