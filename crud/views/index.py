from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from crud.models import Pessoa

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pessoas/select', methods = ['POST'])
def select_pessoas():
    pessoas = Pessoa.query.all()
    data_json = {'data':[{"DT_RowId":f"row_{p.id}", "ID":p.id, "CPF":p.cpf, "NOME":p.nome, "AÇÕES":p.button_actions()} for p in pessoas]}

    return jsonify(data_json)

@main.route('/pessoas/insert', methods = ['POST'])
def insert_pessoa():
    if request.method == 'POST':
        cpf = request.form['cpf']
        nome = request.form['nome']

        pessoa = Pessoa(cpf=cpf, nome=nome)
        try:
            pessoa.insert()

            return 'dados cadastrados com sucesso!'
        except Exception:
            return 'cpf e/ou nome já cadastrado'

        return redirect(url_for('index'))

@main.route('/pessoas/update', methods = ['POST'])
def update_pessoa():
    if request.method == 'POST':
        pessoa = Pessoa.query.filter_by(id=request.form['id']).first()
        pessoa.cpf = request.form['cpf']
        pessoa.nome = request.form['nome']

        try:
            pessoa.update()

            return 'dados alterados com sucesso!'
        except Exception:
            return 'cpf e/ou nome já cadastrado'

        return redirect(url_for('index'))

@main.route('/pessoas/delete', methods = ['POST'])
def delete_pessoa():
    pessoa = Pessoa.query.filter_by(id=int(request.form['id'])).first()
    pessoa.delete()

    return redirect(url_for('index'))