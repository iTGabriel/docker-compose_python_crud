from dotenv import load_dotenv
import os
load_dotenv()
import pymysql.cursors

def criar_conexao():
    if len(os.getenv("DB_ADDRESS")) == 0 and len(os.getenv("DB_USER")) == 0 and len(os.getenv("DB_PASSWORD")) == 0 and len(os.getenv("DB_DATABASE")) == 0:
        return pymysql.connect(host="localhost", user=os.getenv("DB_ROOT_USER"), password=os.getenv("DB_ROOT_PASSWORD"))
    else:
        return pymysql.connect(host=os.getenv("DB_ADDRESS"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), database=os.getenv("DB_DATABASE"))

connection = criar_conexao()

def create_database():
    try:
        cursor = connection.cursor()
        sql = "CREATE DATABASE docker_project;"
        cursor.execute(sql)
    except:
        return

def use_database():
    try:
        cursor = connection.cursor()
        sql = "USE docker_project;"
        cursor.execute(sql)
    except:
        return

def create_table():
    try:
        cursor = connection.cursor()
        sql = "CREATE TABLE tecnologias(id int AUTO_INCREMENT, nome VARCHAR(20), descricao VARCHAR(40), PRIMARY KEY(id));"
        cursor.execute(sql)
        cursor.close()
    except:
        return

def selecionar_todos():
    cursor = connection.cursor()
    sql = "SELECT * FROM `tecnologias`;"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result

def selecionar_um_registro(id=None):
    cursor = connection.cursor()
    sql = "SELECT * FROM `tecnologias` WHERE id=%s;"
    cursor.execute(sql, id)
    result = cursor.fetchall()
    cursor.close()
    return result[0]

def cadastrar_registro(nome=None, descricao=None):
    cursor = connection.cursor()
    sql = "INSERT INTO `tecnologias` (`nome`, `descricao`) VALUES (%s, %s);"
    cursor.execute(sql, (nome, descricao))
    connection.commit()
    cursor.close()

def atualizar_registro(nome=None, descricao=None, id=None):
    cursor = connection.cursor()
    sql = "UPDATE `tecnologias` SET nome=%s,descricao=%s WHERE id=%s;"
    cursor.execute(sql, (nome, descricao, id))
    connection.commit()
    cursor.close()

def deletar_registro(id=None):
    cursor = connection.cursor()
    sql = "DELETE FROM `tecnologias` WHERE id=%s;"
    cursor.execute(sql, id)
    connection.commit()
    cursor.close()

def remover_registros(nome=None, descricao=None):
    try:
        cursor = connection.cursor()
        sql = "TRUNCATE TABLE `tecnologias`;"
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except:
        return

def preparar_db():
    if len(os.getenv("DB_ADDRESS")) == 0 and len(os.getenv("DB_USER")) == 0 and len(os.getenv("DB_PASSWORD")) == 0 and len(os.getenv("DB_DATABASE")) == 0:
            create_database()
            use_database()
            create_table()
            print(
            "\n\n****************************************************************************"
            "\n\n\t\t\t\t- LOCAL -\n"
            "\n\t- Aplicação teste de containers, tecnologias utilizadas logo abaixo "
            "\n\t- Front-end/back-end: Python + flask + jinja2"
            "\n\t- SGBD: mysql"
            "\n\t- Container: Docker "
            "\n\t- Orquestrador: Docker-compose"
            "\n\n\t- Database 'docker_project' criado"
            "\n\t- Tabela 'tecnologias' criadas\n\n"
            "\n****************************************************************************\n")
    else:
        try:
            create_table()
        except:
            print(
            "\n\n****************************************************************************\n"
            "\n\n\t\t\t- CONTAINER / COMPOSE -\n"
            "\n\t- Aplicação teste de containers, tecnologias utilizadas logo abaixo "
            "\n\t- Front-end/back-end: Python + flask + jinja2"
            "\n\t- SGBD: mysql"
            "\n\t- Container: Docker "
            "\n\t- Orquestrador: Docker-compose"
            "\n\n\t- Database 'docker_project' criado"
            "\n\t- Tabela 'tecnologias' criadas\n\n"
            "\n****************************************************************************\n")