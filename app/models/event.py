from datetime import datetime
from app.extensions import db

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    event_date = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    registrations = db.relationship('EventRegistration', backref='event', lazy=True, cascade="all, delete-orphan")

    @staticmethod
    def create(title, description, event_date, capacity):
        event = Event(title=title, description=description, event_date=event_date, capacity=capacity)
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def get_all():
        return Event.query.all()

    @staticmethod
    def get_by_id(event_id):
        return Event.query.get(event_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class EventRegistration(db.Model):
    __tablename__ = 'event_registrations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('user_id', 'event_id', name='_user_event_uc'),)

    @staticmethod
    def create(user_id, event_id):
        registration = EventRegistration(user_id=user_id, event_id=event_id)
        db.session.add(registration)
        db.session.commit()
        return registration

    @staticmethod
    def get_by_user(user_id):
        return EventRegistration.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_id(reg_id):
        return EventRegistration.query.get(reg_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
