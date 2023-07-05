from app import db
class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    receiver_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
