from model.funcoes_simples_db import select_cliente, select_todos_clientes, delete_cliente, update_cliente, insert_cliente, teste_visualizar_tabelas, select_query
from flask import Flask, request



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/cliente/<int:id>", methods=['GET'])
def consulta_cliente(id):
    return select_cliente(id) , 200

# Fun;áo main para teste dos exemplos
def main():

    teste_visualizar_tabelas()

    resp, sucesso = select_cliente(2)

    #resp, sucesso = insert_cliente({'sobrenome':'Soares', 'primeiro_nome':'Rosana', 'cpf':'999.999.999-99'})

    #resp, sucesso = update_cliente(16, {'sobrenome':'do Amaral', 'primeiro_nome':'Tarsila', 'cpf':'999.999.999-99'})

    #resp, sucesso = delete_cliente(16)

    if sucesso:
        print(resp)



if __name__ == '__main__':
    app.run(debug=True)