# Importação das bibliotecas necessárias para trabalhar com MySQL.
import mysql.connector
from mysql.connector import Error

# Função para estabelecer a conexão com o servidor MySQL.
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        # Tenta estabelecer uma conexão usando os detalhes fornecidos (host, usuário, senha).
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        # Se a conexão for bem-sucedida, imprime uma mensagem de sucesso.
        print("Connection to MySQL database successful")
    except Error as err:
        # Se ocorrer um erro durante a tentativa de conexão, imprime a mensagem de erro.
        print(f"Error: '{err}'")

    # Retorna o objeto de conexão para ser usado em outras operações.
    return connection

# Estabelece uma conexão com o servidor MySQL usando os detalhes fornecidos.
connection = create_server_connection("localhost", "myusername", "mypassword")

# Função para criar um banco de dados.
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        # Executa a consulta SQL fornecida (neste caso, para criar um banco de dados).
        cursor.execute(query)
        # Se a consulta for bem-sucedida, imprime uma mensagem de sucesso.
        print("Database created successfully")
    except Error as err:
        # Se ocorrer um erro ao executar a consulta, imprime a mensagem de erro.
        print(f"Error: '{err}'")

# Chama a função `create_database` para criar um novo banco de dados chamado "meuprojeto".
create_database(connection, "CREATE DATABASE meuprojeto")

# Função para executar uma consulta genérica (não finalizada no código fornecido).
def execute_query(connection, query):
    cursor = connection.cursor()
    # Aqui, você adicionaria o código para executar uma consulta (como INSERT, UPDATE, DELETE, etc.) e gerenciar os resultados.
