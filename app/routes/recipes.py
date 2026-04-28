from flask import Blueprint, render_template, request, redirect, url_for, flash

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/')
def index():
    """
    List user's recipe collection.
    Template: recipes/index.html
    """
    pass

@recipes_bp.route('/new', methods=['GET'])
def new_recipe():
    """
    Show form to add a new recipe.
    Template: recipes/edit.html
    """
    pass

@recipes_bp.route('/edit/<int:id>', methods=['GET'])
def edit_recipe(id):
    """
    Show form to edit an existing recipe.
    Template: recipes/edit.html
    """
    pass

@recipes_bp.route('/save', methods=['POST'])
def save_recipe():
    """
    Create or update a recipe.
    Inputs: id (optional), title, ingredients, steps, tags
    Logic: Call Recipe.create() or Recipe.update().
    Output: Redirect to recipes index.
    """
    pass

@recipes_bp.route('/delete/<int:id>', methods=['POST'])
def delete_recipe(id):
    """
    Delete a recipe.
    Logic: Call Recipe.delete().
    Output: Redirect to recipes index.
    """
    pass
