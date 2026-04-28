from datetime import datetime
from app.extensions import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @staticmethod
    def create(user_id, title, description=None, due_date=None):
        task = Task(user_id=user_id, title=title, description=description, due_date=due_date)
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def get_all(user_id=None):
        if user_id:
            return Task.query.filter_by(user_id=user_id).all()
        return Task.query.all()

    @staticmethod
    def get_by_id(task_id):
        return Task.query.get(task_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
