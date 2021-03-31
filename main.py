from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import Data.mysql as mysql_services
import os
app = Flask(__name__)
load_dotenv()


registros = [['1', 'Docker', 'Containers'], ['2', 'Kubernetes', 'Gestão de containers'], ['3', 'Ansible', 'Automação de configurações']]

@app.route('/')
def index():
    registros = mysql_services.selecionar_todos()
    return render_template('index.html', registros=registros)

@app.route('/dados/cadastrar/', methods=['POST'])
def cadastrar_registro():
    nome_tecnologia = request.form['nome_tecnologia']
    descrisao_tecnologia = request.form['descrisao_tecnologia']
    mysql_services.cadastrar_registro(nome_tecnologia,descrisao_tecnologia)
    return redirect(url_for('index'))

@app.route('/dados/editar/<id_registro>', methods=['POST', 'GET'])
def atualizar_registro(id_registro):
    if str(id_registro) == str(mysql_services.selecionar_um_registro(id_registro)[0]):
        nome_tecnologia = request.form['nome_tecnologia']
        descrisao_tecnologia = request.form['descrisao_tecnologia']
        mysql_services.atualizar_registro(nome_tecnologia,descrisao_tecnologia, id_registro)

    return redirect(url_for('index'))


@app.route('/dados/remover/<id_registro>')
def remover_registro(id_registro):
    mysql_services.deletar_registro(id_registro)
    return redirect(url_for('index'))

@app.route('/dados/remover/')
def remover_registros():
    mysql_services.remover_registros()
    return redirect(url_for('index'))

mysql_services.preparar_db()
if __name__ == '__main__':
    app.run(os.getenv("FLASK_ADDRESS"), os.getenv("FLASK_PORT"))