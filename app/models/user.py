from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import db

class User(UserMixin, db.Model):
    """
    User model for storing account credentials and profile info.
    """
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
        """Hashes the password and stores it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the password against the hash."""
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create(username, email, password):
        """Creates a new user record."""
        try:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            print(f"Error creating user: {e}")
            return None

    @staticmethod
    def get_all():
        """Returns all users."""
        return User.query.all()

    @staticmethod
    def get_by_id(user_id):
        """Returns a user by their ID."""
        return User.query.get(user_id)

    def update(self, **kwargs):
        """Updates user attributes dynamically."""
        try:
            for key, value in kwargs.items():
                if key == 'password':
                    self.set_password(value)
                else:
                    setattr(self, key, value)
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            print(f"Error updating user: {e}")
            return None

    def delete(self):
        """Deletes the user record."""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting user: {e}")
            return False
