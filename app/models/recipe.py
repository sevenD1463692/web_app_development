from datetime import datetime
from app.extensions import db

class Recipe(db.Model):
    """
    Recipe model for collecting and managing recipes.
    """
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    ingredients = db.Column(db.Text)
    steps = db.Column(db.Text)
    tags = db.Column(db.String(200))  # Comma-separated tags
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @staticmethod
    def create(user_id, title, ingredients=None, steps=None, tags=None):
        """Creates a new recipe."""
        try:
            recipe = Recipe(user_id=user_id, title=title, ingredients=ingredients, steps=steps, tags=tags)
            db.session.add(recipe)
            db.session.commit()
            return recipe
        except Exception as e:
            db.session.rollback()
            print(f"Error creating recipe: {e}")
            return None

    @staticmethod
    def get_all(user_id=None):
        """Returns all recipes, optionally filtered by user_id."""
        if user_id:
            return Recipe.query.filter_by(user_id=user_id).all()
        return Recipe.query.all()

    @staticmethod
    def get_by_id(recipe_id):
        """Returns a single recipe by its ID."""
        return Recipe.query.get(recipe_id)

    def update(self, **kwargs):
        """Updates recipe details."""
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            print(f"Error updating recipe: {e}")
            return None

    def delete(self):
        """Deletes the recipe."""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting recipe: {e}")
            return False
