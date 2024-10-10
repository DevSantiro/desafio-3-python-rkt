from repository.db.database import db

class Message(db.Model):
    __tablename__ = "message"

    message_id = db.Column(db.Integer, primary_key = True)
    # user_id    = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    message    = db.Column(db.Text,    nullable = False)

    @staticmethod
    def add_message(message):
        print("Salvando a mensagem no banco de dados...")
        msg = Message(message=message)
        db.session.add(msg)
        db.session.commit()
        print("Salvo com sucesso...")
