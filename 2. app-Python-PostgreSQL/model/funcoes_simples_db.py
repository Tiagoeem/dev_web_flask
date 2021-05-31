# Inspiração para INSERT: tutorial oficial da PostegreSQL - https://www.postgresqltutorial.com/postgresql-python/insert/
# Inspiração para UPDATE: tutorial oficial da PostegreSQL - https://www.postgresqltutorial.com/postgresql-python/update/
# Inspiração para DELETE: tutorial oficial da PostegreSQL - https://www.postgresqltutorial.com/postgresql-python/delete/
# Inspiração para SELECT: tutorial oficial da PostegreSQL - https://www.postgresqltutorial.com/postgresql-python/query/
import psycopg2
import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
from config_db import connect



# Utilizado com a operação de INSERT
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


# Utilizado com a operação de UPDATE
def update_query(sql, id_cliente, data_cliente):
    """
    Executa um UPDATE query.\n

    Argumentos:

    sql -- UPDATE SQL Query

    id_cliente -- ID cliente que será atualizado

    data_cliente -- Dicionário com informações sobre o cliente: (Sobrenome, Primeiro Nome, CPF)

    data_cliente = { 'sobrenome': 'da Silva', 'primeiro_nome': 'Tiago', 'cpf':'111.111.111-11' }

    Obs.: CPF no formato string

    Retorno:

    Quantidade de registros alterados
    """
    try:
        # Realiza a conexão com a Base de Dados
        conexao = connect()
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, (data_cliente['sobrenome'], data_cliente['primeiro_nome'], data_cliente['cpf'], id_cliente))
        # Qtd de resgistros alterados
        update_rows = cur.rowcount
        cur.close();
        # Realiza o commit da operação
        conexao.commit()
        # Encerra a conexão
        conexao.close()
    except:
        raise Exception(psycopg2.DatabaseError)
        print(error)
    return update_rows


# Utilizado com a operação de DELETE
def delete_query(sql, id_cliente):
    """
    Executa um DELETE query.\n

    Argumentos:

    sql -- DELETE SQL Query

    id_cliente -- ID cliente que será deletado

    Retorno:

    Quantidade de registros alterados
    """
    try:
        # Realiza a conexão com a Base de Dados
        conexao = connect()
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, (id_cliente,))
        # Qtd de registros deletados
        deleted_rows = cur.rowcount
        cur.close();
        # Realiza o commit da operação
        conexao.commit()
        # Encerra a conexão
        conexao.close()
    except:
        raise Exception(psycopg2.DatabaseError)
        print(error)
    return deleted_rows


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
        raise Exception(psycopg2.DatabaseError)
    # Retorna a resposta da Base de Dados
    return record

# Função criada apenas para fornecer vizualização de todas as tabelas da Base de exemplo
def teste_visualizar_tabelas():
    """
    Apenas uma função de teste que retorna todo o conteudo das três tabelas da Base de Exemplo.
    """  
    
    # Nome das colunas da tabela de clientes
    colunas_clientes = ['sobrenome', 'nome', 'cpf', 'id_cliente']
    # Query para visualização de todos os registros da tabela de clientes
    resp_cli = select_query('Select * from tbl_clientes')

    # Construção de uma lista com os registros convertidos para um dicionário
    lista_dict_cli = []
    for linha in resp_cli:
        lista_dict_cli.append( dict( zip( colunas_clientes, linha) ) )

    # Problemas para entender o que aconteceu aqui com o lista_dict_cli? 
    # Click aqui e simule passo a passo neste notebook no Colab:
    # https://colab.research.google.com/drive/1OhXGNc4E9BeGGRb70ZHhMRj3HU1lwHbI?usp=sharing

    # Exibe lista no console
    print('Tabela Clientes')
    print(lista_dict_cli)
    print('') # Espaço para melhor visibilidade no console
    
    # colocar um notebook aqui!!!!!!!!!@###

    # Nome das colunas da tabela de quartos
    colunas_quartos = ['id_quarto', 'tipo', 'andar', 'tipo_cama', 'n_pessoas_max', 'descricao']
    # Query para visualização de todos os registros da tabela de quartos
    resp_qua = select_query('Select * from tbl_quartos')

    # Construção de uma lista com os registros convertidos para um dicionário
    lista_dict_qua = []
    for linha in resp_qua:
        lista_dict_qua.append( dict( zip( colunas_quartos, linha) ) )

    # Problemas para entender o que aconteceu aqui com o lista_dict_qua? 
    # Click aqui e simule passo a passo neste notebook no Colab:
    # https://colab.research.google.com/drive/1OhXGNc4E9BeGGRb70ZHhMRj3HU1lwHbI?usp=sharing

    # Exibe lista no console
    print('Tabela Quartos')
    print(lista_dict_qua)
    print('') # Espaço para melhor visibilidade no console

    # Nome das colunas da tabela de reserva
    colunas_reservas = ['data_entrada', 'data_saida', 'id_cliente', 'id_quarto', 'id_reserva', 'observacoes']
    # Query para visualização de todos os registros da tabela de reservas
    resp_res = select_query('Select * from tbl_reserva')

    # Construção de uma lista com os registros convertidos para um dicionário
    lista_dict_res = []
    for linha in resp_res:
        lista_dict_res.append( dict( zip( colunas_reservas, linha) ) )

    # Problemas para entender o que aconteceu aqui com o lista_dict_res? 
    # Click aqui e simule passo a passo neste notebook no Colab:
    # https://colab.research.google.com/drive/1OhXGNc4E9BeGGRb70ZHhMRj3HU1lwHbI?usp=sharing

    # Exibe lista no console
    print('Tabela Quartos')
    print(lista_dict_res)
