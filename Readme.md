# Aplicação Flask de Gestão de Frota com PostgreSQL

Pequena aplicação web que permite Listar, adicionar e eliminar carros de uma frota utilizando Python com a blibloteca Flask e tambem Postgresql como base de dados.

## Funcionalidades

- Visualizar Carros existentes
- Adicionar e eliminar Carros com Matriculas únicas

## Pré-requisitos

Antes de executar a aplicação, certifique-se de que tem o seguinte instalado:

- Python 3.x
- Flask
- psycopg2 (adaptador PostgreSQL para Python)
- Base de dados PostgreSQL

## Instalação

- Clone o repositório:
    ```
    git clone https://github.com/JoaoPedroAfonsoSena/DesafioRolearJoaoSena
    cd DesafioRolearJoaoSena
    ```
- Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
- Configure a Base de Dados PostgreSQL

    Pode utilizar o programa pgAdmin4 para correr a base de dados

    Criação da base de dados:
    ```
    CREATE DATABASE frotadecarros
    
    CREATE TABLE IF NOT EXISTS public.frota
    (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    marca text COLLATE pg_catalog."default",
    modelo text COLLATE pg_catalog."default",
    matricula text COLLATE pg_catalog."default",
    CONSTRAINT frota_pkey PRIMARY KEY (id)
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.frota
        OWNER to postgres;
    ```
## Utilização

- Verifique que tem a base de dados configurada corretamente incluindo dentro do ficheiro aplicação_web.py debaixo do comentario "Configuração da Base de Dados".
- Run no ficheiro aplicação_web.py
- Aceda à aplicação no seu navegador. (http://127.0.0.1:5000/)
- Veja os Carros existentes na página inicial.
- Para adicionar um novo Carro, introduza a Marca,Modelo e a Matricula únicas  no formulário fornecido e clique em "Adicionar Carro!".
- Para eliminar um carro clique em "apagar" logo abaixo do registo de cada carro.

## Resolução de Problemas

- Se encontrar algum problema, verifique as mensagens de erro no terminal onde a aplicação Flask está a ser executada.
- Certifique-se de que a sua base de dados PostgreSQL está configurada corretamente.
