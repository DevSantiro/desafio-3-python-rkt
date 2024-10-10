from repository.db.database import db
from flask_login            import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"
    # Definição dos campos no Banco de Dados
    user_id   = db.Column(db.Integer,     primary_key = True)
    username  = db.Column(db.String(80),  nullable = False, unique=True)
    password  = db.Column(db.String(350), nullable = False)
    name      = db.Column(db.String(80),  nullable = False)
