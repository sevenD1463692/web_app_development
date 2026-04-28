from flask import Blueprint, render_template, request, redirect, url_for, flash

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('/')
def index():
    """
    List all tasks for the logged-in user.
    Template: tasks/index.html
    """
    pass

@tasks_bp.route('/add', methods=['POST'])
def add_task():
    """
    Create a new task.
    Inputs: title, description, due_date
    Logic: Call Task.create().
    Output: Redirect to tasks index.
    """
    pass

@tasks_bp.route('/edit/<int:id>', methods=['GET'])
def edit_task(id):
    """
    Show form to edit an existing task.
    Template: tasks/edit.html
    """
    pass

@tasks_bp.route('/update/<int:id>', methods=['POST'])
def update_task(id):
    """
    Update an existing task.
    Inputs: title, description, due_date, is_completed
    Logic: Call Task.update().
    Output: Redirect to tasks index.
    """
    pass

@tasks_bp.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    """
    Delete a task.
    Logic: Call Task.delete().
    Output: Redirect to tasks index.
    """
    pass
