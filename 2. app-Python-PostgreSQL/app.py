from model.funcoes_simples_db import select_query, insert_query, teste_visualizar_tabelas



def main():
    # teste_visualizar_tabelas()
    # resp = exemplo_select_cli(1)
    # resp = exemplo_insert_cli({'sobrenome':'Soares', 'primeiro_nome':'Rosana', 'cpf':'999.999.999-99'})
    resp = 
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
    else:
        dict_resposta = {'Erro': 'Sem correspondencia'}

    return dict_resposta




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
    else:
        dict_resposta = {'Erro': 'Nao foi possivel inserir'}

    return dict_resposta



def exemplo_update_cli(id, dados_cliente):
    
    # Query de exemplo
    #query = 'UPDATE tbl_clientes(sobrenome, primeiro_nome, cpf) VALUES (%s, %s, %s)'
    # Utilizando a função auxiliar para realizar o comando de INSERT
    id_cli = insert_query(query, dados_cliente)
    # Verifica se houve resposta da Base com o resltado da pesquisa
    if id_cli != None:
        # Adiciona id_cliente como chave do dicionário já existente
        dados_cliente['id_cliente'] = id_cli
        dict_resposta = dados_cliente
    else:
        dict_resposta = {'Erro': 'Nao foi possivel inserir'}

    return dict_resposta    



def exemplo_delete_cli(id):
    pass

if __name__ == '__main__':
    main()