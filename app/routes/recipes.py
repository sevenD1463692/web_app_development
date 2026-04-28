from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.recipe import Recipe

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/')
@login_required
def index():
    """
    List user's recipe collection.
    """
    recipes = Recipe.get_all(user_id=current_user.id)
    return render_template('recipes/index.html', recipes=recipes)

@recipes_bp.route('/new', methods=['GET'])
@login_required
def new_recipe():
    """
    Show form to add a new recipe.
    """
    return render_template('recipes/edit.html', recipe=None)

@recipes_bp.route('/edit/<int:id>', methods=['GET'])
@login_required
def edit_recipe(id):
    """
    Show form to edit an existing recipe.
    """
    recipe = Recipe.get_by_id(id)
    if not recipe or recipe.user_id != current_user.id:
        flash('Recipe not found.')
        return redirect(url_for('recipes.index'))
    return render_template('recipes/edit.html', recipe=recipe)

@recipes_bp.route('/save', methods=['POST'])
@login_required
def save_recipe():
    """
    Create or update a recipe.
    """
    recipe_id = request.form.get('id')
    title = request.form.get('title')
    ingredients = request.form.get('ingredients')
    steps = request.form.get('steps')
    tags = request.form.get('tags')
    
    if not title:
        flash('Title is required!')
        return redirect(url_for('recipes.index'))

    if recipe_id:
        recipe = Recipe.get_by_id(int(recipe_id))
        if recipe and recipe.user_id == current_user.id:
            recipe.update(title=title, ingredients=ingredients, steps=steps, tags=tags)
            flash('Recipe updated!')
    else:
        Recipe.create(user_id=current_user.id, title=title, ingredients=ingredients, steps=steps, tags=tags)
        flash('Recipe saved!')
        
    return redirect(url_for('recipes.index'))

@recipes_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_recipe(id):
    """
    Delete a recipe.
    """
    recipe = Recipe.get_by_id(id)
    if not recipe or recipe.user_id != current_user.id:
        flash('Recipe not found.')
        return redirect(url_for('recipes.index'))

    recipe.delete()
    flash('Recipe deleted.')
    return redirect(url_for('recipes.index'))
