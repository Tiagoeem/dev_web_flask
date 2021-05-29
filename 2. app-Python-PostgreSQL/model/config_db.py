from configparser import ConfigParser
from sys import path
import psycopg2
import os


def config(filename='./model/database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    # read connection parameters
    print()

    diretorio_rel = os.path.realpath(os.path.dirname(__file__))
    params = config( os.path.join(diretorio_rel, 'database.ini') )
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
    
    # retorna a conexão
    return conn
