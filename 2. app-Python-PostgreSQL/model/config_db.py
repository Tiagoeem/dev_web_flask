from configparser import ConfigParser
from sys import path
import psycopg2
import os

# Arquivo inspirado no tutorial oficial da PostegreSQL: https://www.postgresqltutorial.com/postgresql-python/connect/

def config(filename='./model/database.ini', section='postgresql'):
    """
    Realiza a leitura dos valores necessários para configuração da conexão com a base PostgreSQL.
    As configurações estão no arquivo database.ini.

    Exemplo de arquivo .ini:\n
    [postgresql]\n
    host=localhost\n
    database=suppliers\n
    user=postgres\n
    password=SecurePass\n

    Argumentos:

    filename -- local do arquivo de configuração da conexão

    section -- Sessão que deve ser buscado no arquivo .ini

    Retorno:

    Se a leitura dos valores for bem sucedida, a função irá retornar um dicionário com os parametros de conexão.
    Caso contrario irá lançar um erro.
    """    
    
    # Criando um parser para interpretar o arquivo .ini
    parser = ConfigParser()
    # Lê o arquivo
    parser.read(filename)

    # Procura pela sessão, como valor padrão ele procura por [postgresql]
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    # Retorna os parametros lidos no arquivo
    return db


def connect():
    """ 
    Realiza a conexão com a base de dados PostgreSql utilizando a biblioteca psycopg2.
    """
    conn = None

    # Realiza a leitura dos parametros de conexão
    diretorio_rel = os.path.realpath(os.path.dirname(__file__))
    params = config( os.path.join(diretorio_rel, 'database.ini') )
    # Conecta-se com a base utilizando o psycopg2. 
    # Documentação completa em https://www.psycopg.org/docs/
    conn = psycopg2.connect(**params)
    
    # Retorna o objeto "conexão"
    return conn
