from sqlalchemy import create_engine, Column, Integer, String, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_pagination import paginate

# engine = create_engine('mysql+pymysql://root:''@localhost/crud_flask', convert_unicode=True)
engine = create_engine('sqlite:///db.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    cpf = Column(String(14), unique=True, nullable=False)
    nome = Column(String(40), unique=True, nullable=False) 

    def __repr__(self):
        return '<Pessoa {}>'.format(self.cpf)

    def select(self, page, limit):
        self.page = page
        self.limit = limit

        pessoas = paginate(db_session.query(self).order_by(desc(self.id)), self.page, self.limit)
        return pessoas

    def insert(self):
        db_session.execute('INSERT INTO pessoa (cpf, nome) VALUES (:param1, :param2)',
        {'param1':self.cpf, 'param2':self.nome})
        db_session.commit()

    def update(self):
        db_session.execute('UPDATE pessoa SET cpf = :param1, nome = :param2 WHERE id = :param3',
        {'param1':self.cpf, 'param2':self.nome, 'param3':self.id})
        db_session.commit()

    def delete(self):
        db_session.execute('DELETE FROM pessoa WHERE id = :param', 
        {'param':self.id})
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()