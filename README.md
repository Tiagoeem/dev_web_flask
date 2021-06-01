# Introdução a microserviços REST

Este repositório foi construído para auxiliar o aluno a compreender o que é um web service REST, fornecendo exemplos, documentação e referências para que o mesmo possa atuar como peça central no aprendizado do assunto em questão.

# Visão geral do repositório

O repositório está basicamente dividido em três modos principais:

- Material de apoio ao conhecimento prévio para acompanhar a aula. (Apesar de serem assuntos já vistos pelos alunos, é sempre interessante ter um material para rápida consulta)
  - [0. conhecimento prévio](https://github.com/Tiagoeem/dev_web_flask/tree/main/0.%20conhecimento%20pr%C3%A9vio): Principais links e documentos com todo o conhecimento prévio necessario para aula.

- Pastas com arquivos necessários para acompanhamento da aula, com diversas etapas para referência do aluno durante o desenvolvimento.
  - [1. ambiente virtual + dump BD](https://github.com/Tiagoeem/dev_web_flask/tree/main/1.%20ambiente%20virtual%20%2B%20dump%20BD): Arquivo requirements.txt para instalação dos pacotes no ambiente virtual e Arquivo Dump da base de dados para criação rápida da Base de Dados utilizada em aula.
  - [2. app-Python-PostgreSQL](https://github.com/Tiagoeem/dev_web_flask/tree/main/2.%20app-Python-PostgreSQL): Aplicação que possui conexão com uma base PostgreSQL, CRUD da tabela de clientes completamente funcional, deve ser usado no terminal.
  - [3. app-HelloWorld-Flask](https://github.com/Tiagoeem/dev_web_flask/tree/main/3.%20app-HelloWorld-Flask): Aplicação mais simples possivel para execução do Flask, retirado da propria [documentação](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
  - [4. app-Flask-ProstgreSQL(finalizado)](https://github.com/Tiagoeem/dev_web_flask/tree/main/4.%20app-Flask-ProstgreSQL(finalizado)): Aplicação REST utilizando Flask e PostgreSQL, rotas de teste e CRUD de clientes.
  - [5. app-Em-Sala](https://github.com/Tiagoeem/dev_web_flask/tree/main/5.%20app-Em-Sala): Ponto de partida na sala de aula, esse código idealmente deve sair da versão 2. e chegar até a 4.

- Material complementar com o intuito de apresentar ao alunos a continuação do caminho de aprendizado em cada uma das dimensões apresentadas na aula.
  - [6. material complementar](https://github.com/Tiagoeem/dev_web_flask/tree/main/6.%20material%20complementar): Links separados por assuntos, com documentações e tutoriais para a evolução do trabalho realizado em aula.

# O problema

Como o Skyscanner encontra hoteis nas mais diversas plataformas de busca e booking?

![image](https://user-images.githubusercontent.com/25457273/120265745-01addb80-c277-11eb-8d7a-98f8348d867d.png)

Como o site/sistema deles é capaz de se comunicar com outros sistemas de reservas de quartos? ([getaroom](https://www.getaroom.com/), [Trip.com](https://br.trip.com/?locale=pt_br), [booking.com](https://www.booking.com/index.html?aid=1382154&label=98b039b6c28f11eb8e469e4b97b7f317) etc)

Discutiremos em aula maneiras de comunicar sistemas web através da internet, de forma organizada e padronizada.

# Exemplo em sala

Baseado nas aulas anteriores, iniciaremos a aula com um código exatamente igual ao encotrado na pasta [2. app-Python-PostgreSQL](https://github.com/Tiagoeem/dev_web_flask/tree/main/2.%20app-Python-PostgreSQL). Este códito é capaz de conectar-se a uma Base de Dados (local, se o arquivo .ini for mantido) PostgreSQL, sem o auxilio de [ORMs](https://www.fullstackpython.com/object-relational-mappers-orms.html) como [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) para não adicionar camadas de abstração e complexidades desnecessárias.

Conceitos de **Programação Orientação a Objetos (POO)** e ***Design Patterns*** seão apresentadas posteriormente no curso e então ORMs farão todo sentido para nós.

Enquanto isso faremos a conexão com a Base de Dados atraves da lib [psycopg2](https://pypi.org/project/psycopg2/) e as funções auxiliares estão escritas com o paradgma estruturado.

## O sistema

O sistema que será trabalhado em sala é de um "micro" hotel, que possuí registro dos quartos que possuem, clientes e reservas. No nosso exemplo trabalharemos principalemente focado na tabela de clientes.

## A Base

O DB utilizado na aula **hotel_dev** possui 3 tabelas: tbl_clientes, tbl_quartos e tbl_reserva. Na imagem abaixo é possivel observar os campos e as relações entre elas. Para carregar em sua base, utilize o dump da base que esta na pasta [1. ambiente virtual + dump BD](https://github.com/Tiagoeem/dev_web_flask/tree/main/1.%20ambiente%20virtual%20%2B%20dump%20BD).

![image](https://user-images.githubusercontent.com/25457273/120267232-ef816c80-c279-11eb-8245-80db13569d12.png)

### tbl_clientes

![image](https://user-images.githubusercontent.com/25457273/120267464-5dc62f00-c27a-11eb-8575-1f3b7573a8de.png)

### tbl_quartos

![image](https://user-images.githubusercontent.com/25457273/120267513-759db300-c27a-11eb-98f7-ed209fff63a1.png)

### tbl_reserva

![image](https://user-images.githubusercontent.com/25457273/120267546-89491980-c27a-11eb-842b-4cea3ba9aca6.png)

## Os arquivos .py

- app.py: Arquivo principal
- model/cofig_db.py: Arquivo que auxiliar na conexão com a Base de Dados
- model/funcoes_simples_db.py: Como o nome indica, é um módulo de funções que auxiliam a manipulação das tabelas da Base de Dados. Abstraem operações como SELECT, INSERT, UPDATE e DELETE






