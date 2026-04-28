from datetime import datetime
from app.extensions import db

class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_title = db.Column(db.String(200), nullable=False)
    chapter = db.Column(db.String(100))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @staticmethod
    def create(user_id, book_title, chapter=None, content=None):
        note = Note(user_id=user_id, book_title=book_title, chapter=chapter, content=content)
        db.session.add(note)
        db.session.commit()
        return note

    @staticmethod
    def get_all(user_id=None):
        if user_id:
            return Note.query.filter_by(user_id=user_id).all()
        return Note.query.all()

    @staticmethod
    def get_by_id(note_id):
        return Note.query.get(note_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
