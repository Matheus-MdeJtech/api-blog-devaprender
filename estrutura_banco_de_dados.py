from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Users\Matheus\Documents\PYTHON\Projeto API\api-blog-devaprender
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Matheus/Documents/PYTHON/Projeto API/api-blog-devaprender/blog.db'
db = SQLAlchemy(app)
db: SQLAlchemy




class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    pstagens = db.relationship('Postagem')

def inicializar_banco():
    db.drop_all()
    db.create_all()

    autor = Autor(nome='Matheus', email='matheusrdj13@gmail.com', senha='123456', admin=True)
    db.session.add(autor)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        inicializar_banco()
