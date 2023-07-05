from app import db
from bcrypt import hashpw, checkpw, gensalt

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    confirm_password = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='user', lazy=True)
    sender = db.relationship('Message', backref='user', lazy=True)
    receiver = db.relationship('Message', backref='user', lazy=True)


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def set_password(self, password):
        hashed_password = hashpw(password.encode('utf-8'), gensalt())
        self.password = hashed_password.decode('utf-8')

    def check_password(self, password):
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))