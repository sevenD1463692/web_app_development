from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.task import Task

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('/')
@login_required
def index():
    """
    List all tasks for the logged-in user.
    """
    all_tasks = Task.get_all(user_id=current_user.id)
    return render_template('tasks/index.html', tasks=all_tasks)

@tasks_bp.route('/add', methods=['POST'])
@login_required
def add_task():
    """
    Create a new task.
    """
    title = request.form.get('title')
    description = request.form.get('description')
    due_date_str = request.form.get('due_date')
    
    if not title:
        flash('Title is required!')
        return redirect(url_for('tasks.index'))

    # Basic date parsing (simplified for MVP)
    from datetime import datetime
    due_date = None
    if due_date_str:
        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.')

    Task.create(user_id=current_user.id, title=title, description=description, due_date=due_date)
    flash('Task added successfully!')
    return redirect(url_for('tasks.index'))

@tasks_bp.route('/edit/<int:id>', methods=['GET'])
@login_required
def edit_task(id):
    """
    Show form to edit an existing task.
    """
    task = Task.get_by_id(id)
    if not task or task.user_id != current_user.id:
        flash('Task not found.')
        return redirect(url_for('tasks.index'))
    return render_template('tasks/edit.html', task=task)

@tasks_bp.route('/update/<int:id>', methods=['POST'])
@login_required
def update_task(id):
    """
    Update an existing task.
    """
    task = Task.get_by_id(id)
    if not task or task.user_id != current_user.id:
        flash('Task not found.')
        return redirect(url_for('tasks.index'))

    title = request.form.get('title')
    description = request.form.get('description')
    is_completed = True if request.form.get('is_completed') else False
    
    task.update(title=title, description=description, is_completed=is_completed)
    flash('Task updated!')
    return redirect(url_for('tasks.index'))

@tasks_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_task(id):
    """
    Delete a task.
    """
    task = Task.get_by_id(id)
    if not task or task.user_id != current_user.id:
        flash('Task not found.')
        return redirect(url_for('tasks.index'))

    task.delete()
    flash('Task deleted.')
    return redirect(url_for('tasks.index'))
