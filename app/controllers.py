from app import app
from flask import render_template, request, redirect, url_for, flash
from app.models import Pessoa


@app.route('/')
def index():
    page = request.args.get('p', 1, type=int)
    pessoas = Pessoa.select(Pessoa, page, 5)

    return render_template('index.html', pessoas=pessoas)

@app.route('/insert.pessoa', methods = ['POST'])
def insert_pessoa():
    if request.method == 'POST':
        cpf = request.form['cpf']
        nome = request.form['nome']

        pessoa = Pessoa(cpf=cpf, nome=nome)
        try:
            pessoa.insert()

            flash('dados cadastrados com sucesso!', 'alert-success')
        except Exception:
            flash('cpf e/ou nome já cadastrado', 'alert-danger')

        return redirect(url_for('index'))

@app.route('/update.pessoa', methods = ['POST'])
def update_pessoa():
    if request.method == 'POST':
        pessoa = Pessoa.query.filter_by(id=request.form['id']).first()
        pessoa.cpf = request.form['cpf']
        pessoa.nome = request.form['nome']

        try:
            pessoa.update()

            flash('dados alterados com sucesso!', 'alert-success')
        except Exception:
            flash('cpf e/ou nome já cadastrado', 'alert-danger')

        return redirect(url_for('index'))

@app.route('/delete.pessoa/<int:id>')
def delete_pessoa(id):
    pessoa = Pessoa.query.filter_by(id=id).first()
    pessoa.delete()

    return redirect(url_for('index'))