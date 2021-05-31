from model.funcoes_simples_db import select_cliente, select_todos_clientes, delete_cliente, update_cliente, insert_cliente, teste_visualizar_tabelas, select_query
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/cliente/', methods=['GET'])
def rota_selecionar_todos_clientes():
    # Função que realiza a qeury para selecionar todos os clientes
    resp_cli, sucesso = select_todos_clientes()

    if sucesso:
        # Construção de uma lista com os registros convertidos para um dicionário
        return jsonify(resp_cli), 200
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



# A partir daqui somente rotas de testes com propósito didático, não use como exemplo

# Apenas rota de teste, pode ser removida posteriormente
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Apenas rota de teste e exemplo, pode ser removida posteriormente
@app.route("/teste_recurso/<int:valor>" )
def funcao_teste_recurso(valor):
    return str(valor)

# Apenas rota de teste e exemplo, pode ser removida posteriormente
@app.route("/teste_status/<int:valor>" )
def funcao_teste_status(valor):
    return str(valor), 203

# Apenas rota de teste e exemplo, pode ser removida posteriormente
@app.route("/teste_metodo/<int:valor>", methods=['PUT', 'POST'] )
def funcao_teste_metodo(valor):
    content = request.data
    return str(valor) + ' Metodo PUT' + str(content)

if __name__ == '__main__':
    app.run(debug=True)