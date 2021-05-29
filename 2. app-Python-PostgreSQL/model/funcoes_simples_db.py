import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from config_db import connect

# Utilizado para as operações de INSERT, UPDATE e DELETE
def executar_query(sql):
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
    try:
        conexao = connect()
        cur = conexao.cursor()
        if id==None:
            print(2)
            cur.execute(sql)
        else:
            print(1)
            cur.execute(sql, str(id))
        record = cur.fetchall()
        cur.close();
        conexao.close()
    except:
        return False
    return record


def teste_visualizar_tabelas():
    
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