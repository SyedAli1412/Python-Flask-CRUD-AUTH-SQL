from app import db
from bcrypt import hashpw, checkpw, gensalt

class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    confirm_password = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='user', lazy=True)
    sender = db.relationship('Message', backref='sender', lazy=True, foreign_keys='Message.sender_id')
    receiver = db.relationship('Message', backref='receiver', lazy=True, foreign_keys='Message.receiver_id')

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def set_password(self, password):
        hashed_password = hashpw(password.encode('utf-8'), gensalt())
        self.password = hashed_password.decode('utf-8')

    def check_password(self, password):
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
