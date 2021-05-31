from flask.typing import StatusCode
from model.funcoes_simples_db import select_query, insert_query, update_query, delete_query, teste_visualizar_tabelas
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/teste_rota/<int:post_id>",  )
def funcao_rota_teste():
    return "<p>Somente um teste!</p>"

@app.route('/cliente', methods=['GET'])
def selecionar_todos_clientes():
    colunas_clientes = ['sobrenome', 'nome', 'cpf', 'id_cliente']
    # Query para visualização de todos os registros da tabela de clientes
    resp_cli = select_query('Select * from tbl_clientes')

    # Construção de uma lista com os registros convertidos para um dicionário
    lista_dict_cli = []
    for linha in resp_cli:
        lista_dict_cli.append( dict( zip( colunas_clientes, linha) ) )

    return jsonify(lista_dict_cli), 200


@app.route('/cliente/<int:id>', methods=['GET'])
def selecionar_cliente( id ):
    # Query de exemplo
    query = 'Select * from tbl_clientes WHERE id_cliente = %s'
    # Utilizando a função auxiliar para realizar o comando de SELECT
    resp_cli = select_query(query, id)
    # Verifica se houve resposta da Base com o resltado da pesquisa
    if resp_cli != None:
        # Cria um dicionário com a resposta
        colunas = ['sobrenome', 'nome', 'cpf', 'id_cliente']
        dict_resposta = dict( zip( colunas, resp_cli) ) 
        # Problemas para entender o que aconteceu aqui com o dict_resposta? 
        # Click aqui e simule passo a passo neste notebook no Colab:
        # https://colab.research.google.com/drive/1OhXGNc4E9BeGGRb70ZHhMRj3HU1lwHbI?usp=sharing
        s_code = 200
    else:
        dict_resposta = {'Erro': 'Sem correspondencia'}
        s_code = 404

    return dict_resposta, s_code


@app.route('/cliente', methods=['POST'])
def inserir_cliente():
    try:
        content = request.get_json()
    except:
        return {'Erro': 'Entrada não é um Json Válido'}, 400

    resp, error = exemplo_insert_cli(content)
    if error:
        return resp, 500
    else:
        return resp, 201



# Função main para teste dos exemplos
def main():
    teste_visualizar_tabelas()

    resp = exemplo_select_cli(2)

    #resp = exemplo_insert_cli({'sobrenome':'Soares', 'primeiro_nome':'Rosana', 'cpf':'999.999.999-99'})

    #resp = exemplo_update_cli(3, {'sobrenome':'do Amaral', 'primeiro_nome':'Tarsila', 'cpf':'999.999.999-99'})

    #resp = exemplo_delete_cli(3)

    print(resp)



# Função com exemplo de uso para a função auxiliar select_query
def exemplo_select_cli(id):

    # Query de exemplo
    query = 'Select * from tbl_clientes WHERE id_cliente = %s'
    # Utilizando a função auxiliar para realizar o comando de SELECT
    resp_cli = select_query(query, id)
    # Verifica se houve resposta da Base com o resltado da pesquisa
    if resp_cli != None:
        # Cria um dicionário com a resposta
        colunas = ['sobrenome', 'nome', 'cpf', 'id_cliente']
        dict_resposta = dict( zip( colunas, resp_cli) ) 
        # Problemas para entender o que aconteceu aqui com o dict_resposta? 
        # Click aqui e simule passo a passo neste notebook no Colab:
        # https://colab.research.google.com/drive/1OhXGNc4E9BeGGRb70ZHhMRj3HU1lwHbI?usp=sharing
        erro = False
    else:
        dict_resposta = {'Erro': 'Sem correspondencia'}
        erro = True

    return dict_resposta, erro



# Função com exemplo de uso para a função auxiliar insert_query
def exemplo_insert_cli(dados_cliente):

    # Query de exemplo
    query = 'INSERT INTO tbl_clientes(sobrenome, primeiro_nome, cpf) VALUES (%s, %s, %s)'
    # Utilizando a função auxiliar para realizar o comando de INSERT
    id_cli = insert_query(query, dados_cliente)
    # Verifica se houve resposta da Base com o resltado da pesquisa
    if id_cli != None:
        # Adiciona id_cliente como chave do dicionário já existente
        dados_cliente['id_cliente'] = id_cli
        dict_resposta = dados_cliente
        erro = False
    else:
        dict_resposta = {'Erro': 'Nao foi possivel inserir'}
        erro = True

    return dict_resposta, erro



# Exemplo de uso do UPDATE
# Para fins didaticos será considerado que sempre será atualizado todos os valores do registro
# portanto não havera verificações sobre o conteudo do parâmetro  dados_cliente
def exemplo_update_cli(id, dados_cliente):
    
    # Query de exemplo
    query = 'UPDATE tbl_clientes SET sobrenome = %s, primeiro_nome = %s, cpf = %s WHERE id_cliente = %s'
    # Utilizando a função auxiliar para realizar o comando de UPDATE
    qtd_alterada = update_query(query, id, dados_cliente)
    # Verifica se houve resposta da Base com o resltado da pesquisa
    if qtd_alterada > 0:
        # Adiciona id_cliente como chave do dicionário já existente
        dict_resposta = dados_cliente
    else:
        dict_resposta = {'Erro': 'Nao foi possivel alterar o registro'}

    return dict_resposta



def exemplo_delete_cli(id):
    # Query de exemplo
    query = 'DELETE from tbl_clientes WHERE id_cliente = %s'
    # Utilizando a função auxiliar para realizar o comando de DELETE
    qtd_deletados = delete_query(query, id)
    # Verifica se houve resposta da Base com o resltado da pesquisa
    dict_resposta = {'Registros_Deletados': qtd_deletados }

    return dict_resposta



if __name__ == '__main__':
    app.run(debug=True)