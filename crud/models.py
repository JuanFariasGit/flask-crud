from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pessoa(db.Model):
    __tablename__ = 'pessoa'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    nome = db.Column(db.String(40), unique=True, nullable=False) 

    def __repr__(self):
        return '<Pessoa {}>'.format(self.cpf)

    def button_actions(self):
        return f'<button class="btn btn-sm btn-primary" onclick="editar({self.id})"><i class="far fa-edit fa-lg"></i></button> <button class="btn btn-sm btn-danger" onclick="deletar({self.id})"><i class="far fa-trash-alt fa-lg"></i></button>'
    
    def insert(self):
        db.session.execute('INSERT INTO pessoa (cpf, nome) VALUES (:param1, :param2)',
        {'param1':self.cpf, 'param2':self.nome})
        db.session.commit()

    def update(self):
        db.session.execute('UPDATE pessoa SET cpf = :param1, nome = :param2 WHERE id = :param3',
        {'param1':self.cpf, 'param2':self.nome, 'param3':self.id})
        db.session.commit()

    def delete(self):
        db.session.execute('DELETE FROM pessoa WHERE id = :param', 
        {'param':self.id})
        db.session.commit()