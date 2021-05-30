import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from config_db import connect

# Utilizado para as operações de INSERT, UPDATE e DELETE
def executar_query(sql):
    """
    Executa a query de uma conexão PostgreSQL.\n
    Operações suportadas: INSERT, UPDATE e DELETE

    Argumentos:

    sql -- Query SQL

    Retorno:

    Definir.
    """

    try:
        conexao = connect()
        cur = conexao.cursor()
        cur.execute(sql)
        cur.close();
        conexao.commit()
        conexao.close()
    except:
        return False
    return True

# Utilizado com a operação de SELECT
def select_query(sql, id=None):
    """
    Executa um SELECT query em uma conexão PostgreSQL.\n

    Argumentos:

    sql -- SELECT Query SQL (por simplificação, não existe verificação)

    id -- Valor a ser buscado, se None, retorna tudo

    Retorno:

    Registros
    """    
    try:
        # Realiza a conexão com a Base de Dados
        conexao = connect()
        cur = conexao.cursor()
        if id==None:
            # Executa a query
            cur.execute(sql)
            # Busca todos os registros
            record = cur.fetchall()
        else:
            # Forma segura que passar parâmetro para uma query SQL
            # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
            # Executa a query
            cur.execute(sql, str(id))
            # Busca apenas um registro
            record = cur.fetchone()
        # fecha a conexão
        cur.close();
        conexao.close()
    except:
        return False
    # Retorna a resposta da Base de Dados
    return record


def teste_visualizar_tabelas():
    """
    Apenas uma função de teste que retorna todo o conteudo das três tabelas da Base de Exemplo.
    """  
    
    # tbl_clientes
    colunas_clientes = ['sobrenome', 'nome', 'cpf', 'id_cliente']
    resp_cli = select_query('Select * from tbl_clientes')
    lista_dict_cli = []
    for linha in resp_cli:
        lista_dict_cli.append( dict( zip( colunas_clientes, linha) ) )

    print(lista_dict_cli)
    # problemas para entender o que aconteceu aqui? Click aqui e simule passo a passo:
    # colocar um notebook aqui!!!!!!!!!@###

    # tbl_quartos
    colunas_quartos = ['id_quarto', 'tipo', 'andar', 'tipo_cama', 'n_pessoas_max', 'descricao']
    resp_qua = select_query('Select * from tbl_quartos')
    lista_dict_qua = []
    for linha in resp_qua:
        lista_dict_qua.append( dict( zip( colunas_quartos, linha) ) )

    print(lista_dict_qua)


    # tbl_reservas
    colunas_reservas = ['data_entrada', 'data_saida', 'id_cliente', 'id_quarto', 'id_reserva', 'observacoes']
    resp_res = select_query('Select * from tbl_reserva')
    lista_dict_res = []
    for linha in resp_res:
        lista_dict_res.append( dict( zip( colunas_reservas, linha) ) )

    print(lista_dict_res)