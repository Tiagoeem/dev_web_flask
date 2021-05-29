from model.funcoes_simples_db import executar_query, select_query, teste_visualizar_tabelas


def main():
    #teste_visualizar_tabelas()
    resp = exemplo_select_cli(0)
    print(resp)


def exemplo_select_cli(id):

    query = 'Select * from tbl_clientes WHERE id_cliente = %s'
    resp_cli = select_query(query, id)
    if len(resp_cli) > 0:
        colunas = ['sobrenome', 'nome', 'cpf', 'id_cliente']
        dict_resposta = dict( zip( colunas, resp_cli[0]) ) 
        print(dict_resposta)
    else:
        dict_resposta = dict( 0, 0 )
        print('Sem correspondencia')

    return dict_resposta

def exemplo_insert_cli( dados ):

    #valores = (5, 'One Plus 6', 950)
    #cursor.execute(postgres_insert_query, record_to_insert)
    pass

def exemplo_update_cli(id, dados):
    pass

def exemplo_delete_cli(id):
    pass

if __name__ == '__main__':
    main()