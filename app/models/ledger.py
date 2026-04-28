from datetime import datetime
from app.extensions import db

class LedgerEntry(db.Model):
    """
    LedgerEntry model for personal accounting (income/expense).
    """
    __tablename__ = 'ledger_entries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'income' or 'expense'
    category = db.Column(db.String(50))
    entry_date = db.Column(db.Date, nullable=False, default=datetime.utcnow().date())
    note = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (
        db.CheckConstraint(type.in_(['income', 'expense']), name='check_ledger_type'),
    )

    @staticmethod
    def create(user_id, amount, type, category=None, entry_date=None, note=None):
        """Records a new financial transaction."""
        try:
            if not entry_date:
                entry_date = datetime.utcnow().date()
            entry = LedgerEntry(user_id=user_id, amount=amount, type=type, category=category, entry_date=entry_date, note=note)
            db.session.add(entry)
            db.session.commit()
            return entry
        except Exception as e:
            db.session.rollback()
            print(f"Error creating ledger entry: {e}")
            return None

    @staticmethod
    def get_all(user_id=None):
        """Returns all entries, optionally filtered by user_id and sorted by date."""
        if user_id:
            return LedgerEntry.query.filter_by(user_id=user_id).order_by(LedgerEntry.entry_date.desc()).all()
        return LedgerEntry.query.all()

    @staticmethod
    def get_by_id(entry_id):
        """Returns a single entry by its ID."""
        return LedgerEntry.query.get(entry_id)

    def update(self, **kwargs):
        """Updates entry attributes."""
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            print(f"Error updating ledger entry: {e}")
            return None

    def delete(self):
        """Deletes the entry."""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting ledger entry: {e}")
            return False
