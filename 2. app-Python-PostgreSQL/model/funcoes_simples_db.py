# Inspiração para Insert, tutorial oficial da PostegreSQL: https://www.postgresqltutorial.com/postgresql-python/insert/
import psycopg2
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


def insert_query(sql, data_cliente):
    """
    Executa um INSERT query.\n

    Argumentos:

    sql -- INSERT SQL Query

    data_cliente -- Dicionário com informações sobre o cliente: (Sobrenome, Primeiro Nome, CPF)

    data_cliente = { 'sobrenome': 'da Silva', 'primeiro_nome': 'Tiago', 'cpf':'111.111.111-11' }

    Obs.: CPF no formato string

    Retorno:

    ID gerado automaticamente pela base
    """
    # Estamos adicionando essa linha para que após a inserção do registro
    # seja retorna o id do cliente adicionado
    sql = sql + ' RETURNING id_cliente'
    try:
        # Realiza a conexão com a Base de Dados
        conexao = connect()
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, (data_cliente['sobrenome'], data_cliente['primeiro_nome'], data_cliente['cpf']))
        # Recupera o valor do id_cliente gerado automaticamente pela base
        id_cliente = cur.fetchone()[0]
        print(id_cliente)
        cur.close();
        # Realiza o commit da operação
        conexao.commit()
        # Encerra a conexão
        conexao.close()
    except:
        raise Exception(psycopg2.DatabaseError)
        print(error)
    return id_cliente

# Utilizado com a operação de SELECT
def select_query(sql, id=None):
    """
    Executa um SELECT query em uma conexão PostgreSQL.\n

    Argumentos:

    sql -- SELECT Query SQL (por simplificação, não existe verificação)

    id -- Valor a ser buscado, se None, retorna tudo

    Retorno:

    Registros da tabela na Base de exemplo
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
        # Encerra a conexão
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