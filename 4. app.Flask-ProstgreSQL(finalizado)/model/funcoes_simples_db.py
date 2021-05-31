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
def insert_query(sql, data):
    """
    Executa um INSERT query.\n

    Argumentos:

    sql -- INSERT SQL Query

    data -- Dicionário com informações. Exemplo.: cliente: (Sobrenome, Primeiro Nome, CPF)

    data = { 'sobrenome': 'da Silva', 'primeiro_nome': 'Tiago', 'cpf':'111.111.111-11' } (Exemplo)

    Obs.: CPF no formato string

    Retorno:

    ID gerado automaticamente pela base e indicação de sucesso (True/False)
    """
    # Estamos adicionando essa linha para que após a inserção do registro
    # seja retorna o id do cliente adicionado
    sucesso = True
    sql = sql + ' RETURNING id_cliente'
    try:
        # Realiza a conexão com a Base de Dados
        conexao = connect()
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, data)
        # Recupera o valor do id_cliente gerado automaticamente pela base
        id_cliente = cur.fetchone()[0]
        print(id_cliente)
        cur.close();
        # Realiza o commit da operação
        conexao.commit()
        # Encerra a conexão
        conexao.close()
    except:
        sucesso = False
        print(psycopg2.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
        
    return id_cliente, sucesso


# Utilizado com a operação de UPDATE
def update_query(sql, data):
    """
    Executa um UPDATE query.\n

    Argumentos:

    sql -- UPDATE SQL Query

    id -- ID cliente que será atualizado

    data -- Dicionário com informações. Exemplo.: cliente: (Sobrenome, Primeiro Nome, CPF)

    data = { 'sobrenome': 'da Silva', 'primeiro_nome': 'Tiago', 'cpf':'111.111.111-11' } (Exemplo)

    Obs.: CPF no formato string

    Retorno:

    Quantidade de registros alterados e indicação de sucesso (True/False)
    """
    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = connect()
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, data )
        # Qtd de resgistros alterados
        update_rows = cur.rowcount
        cur.close();
        # Realiza o commit da operação
        conexao.commit()
        # Encerra a conexão
        conexao.close()
    except:
        update_rows = 0
        sucesso = False
        print(psycopg2.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    return update_rows, sucesso


# Utilizado com a operação de DELETE
def delete_query(sql, id):
    """
    Executa um DELETE query.\n

    Argumentos:

    sql -- DELETE SQL Query

    id_cliente -- ID cliente que será deletado

    Retorno:

    Quantidade de registros alterados e indicação de sucesso (True/False)
    """
    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = connect()
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, (id,))
        # Qtd de registros deletados
        deleted_rows = cur.rowcount
        cur.close();
        # Realiza o commit da operação
        conexao.commit()
        # Encerra a conexão
        conexao.close()
    except:
        sucesso = False
        print(psycopg2.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    return deleted_rows, sucesso


# Utilizado com a operação de SELECT
def select_query(sql, id=0):
    """
    Executa um SELECT query em uma conexão PostgreSQL.\n

    Argumentos:

    sql -- SELECT Query SQL (por simplificação, não existe verificação)

    id -- Valor a ser buscado, se None, retorna tudo

    Retorno:

    Registros da tabela na Base de exemplo e indicação de sucesso (True/False)
    """
    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = connect()
        cur = conexao.cursor()
        if id==0:
            # Executa a query
            cur.execute(sql)
            # Busca todos os registros
            record = cur.fetchall()
        else:
            # Forma segura que passar parâmetro para uma query SQL
            # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
            # Executa a query
            cur.execute(sql, (id,))
            # Busca apenas um registro
            record = cur.fetchone()
        # Se não encontrou nenhum registro, sucesso é False. 
        # Atenção: Não encontrar registro não gera erro, por isso não irá passar pelo "except"
        if record==None:
            sucesso = False
        # Encerra a conexão
        cur.close();
        conexao.close()
    except:
        sucesso = False
        record = None
        print(psycopg2.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    # Retorna a resposta da Base de Dados
    return record, sucesso

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


    # Função com exemplo de uso para a função auxiliar select_query
def select_cliente(id):

    # Query de exemplo
    query = 'Select * from tbl_clientes WHERE id_cliente = %s'
    # Utilizando a função auxiliar para realizar o comando de SELECT
    resp_cli, sucesso = select_query(query, id)
    # Verifica se houve resposta da Base com o resltado da pesquisa
    if sucesso:
        # Cria um dicionário com a resposta
        colunas = ['sobrenome', 'nome', 'cpf', 'id_cliente']
        dict_resposta = dict( zip( colunas, resp_cli) ) 
        # Problemas para entender o que aconteceu aqui com o dict_resposta? 
        # Click aqui e simule passo a passo neste notebook no Colab:
        # https://colab.research.google.com/drive/1OhXGNc4E9BeGGRb70ZHhMRj3HU1lwHbI?usp=sharing
    else:
        dict_resposta = {'Erro': 'Sem correspondencia'}

    return dict_resposta, sucesso



# Função com exemplo de uso para a função auxiliar insert_query
def insert_cliente(dados_cliente):

    # Query de exemplo
    query = 'INSERT INTO tbl_clientes(sobrenome, primeiro_nome, cpf) VALUES (%s, %s, %s)'
    # Utilizando a função auxiliar para realizar o comando de INSERT
    id_cli, sucesso = insert_query(query, list(dados_cliente.values()))
    # Verifica se houve resposta da Base com o resltado da pesquisa
    if sucesso:
        # Adiciona id_cliente como chave do dicionário já existente
        dados_cliente['id_cliente'] = id_cli
        dict_resposta = dados_cliente
    else:
        dict_resposta = {'Erro': 'Nao foi possivel inserir'}

    return dict_resposta, sucesso



# Exemplo de uso do UPDATE
# Para fins didaticos será considerado que sempre será atualizado todos os valores do registro
# portanto não havera verificações sobre o conteudo do parâmetro  dados_cliente
def update_cliente(id, dados_cliente):
    
    # Query de exemplo
    query = 'UPDATE tbl_clientes SET sobrenome = %s, primeiro_nome = %s, cpf = %s WHERE id_cliente = %s'
    # Utilizando a função auxiliar para realizar o comando de UPDATE
    all_data = list(dados_cliente.values())
    all_data.append(str(id))
    qtd_alterada, sucesso = update_query(query, all_data )
    # Verifica se houve resposta da Base com o resltado da pesquisa
    if sucesso:
        # Adiciona id_cliente como chave do dicionário já existente
        dict_resposta = dados_cliente
    else:
        dict_resposta = {'Erro': 'Nao foi possivel alterar o registro'}

    return dict_resposta, sucesso


# Exemplo de uso do DELETE
def delete_cliente(id):
    # Query de exemplo
    query = 'DELETE from tbl_clientes WHERE id_cliente = %s'
    # Utilizando a função auxiliar para realizar o comando de DELETE
    qtd_deletados, sucesso = delete_query(query, id)
    # Verifica se houve resposta da Base com o resultado da pesquisa
    dict_resposta = {'Registros_Deletados': qtd_deletados }

    return dict_resposta, sucesso


def select_todos_clientes():
    colunas_clientes = ['sobrenome', 'nome', 'cpf', 'id_cliente']
    # Query para visualização de todos os registros da tabela de clientes
    resp_cli, sucesso = select_query('Select * from tbl_clientes')

    if sucesso:
        # Construção de uma lista com os registros convertidos para um dicionário
        lista_dict_cli = []
        for linha in resp_cli:
            lista_dict_cli.append( dict( zip( colunas_clientes, linha) ) )
        # Problemas para entender o que aconteceu aqui com o dict_resposta? 
        # Click aqui e simule passo a passo neste notebook no Colab:
        # https://colab.research.google.com/drive/1OhXGNc4E9BeGGRb70ZHhMRj3HU1lwHbI?usp=sharing
        return lista_dict_cli, sucesso
    else:
        dict_resposta = {'Erro': 'Sem correspondencia'}
        return dict_resposta, sucesso
    