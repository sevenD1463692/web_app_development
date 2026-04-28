from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    tasks = db.relationship('Task', backref='user', lazy=True, cascade="all, delete-orphan")
    ledger_entries = db.relationship('LedgerEntry', backref='user', lazy=True, cascade="all, delete-orphan")
    notes = db.relationship('Note', backref='user', lazy=True, cascade="all, delete-orphan")
    registrations = db.relationship('EventRegistration', backref='user', lazy=True, cascade="all, delete-orphan")
    recipes = db.relationship('Recipe', backref='user', lazy=True, cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create(username, email, password):
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'password':
                self.set_password(value)
            else:
                setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
