from flask import Blueprint, render_template, request, redirect, url_for, flash

notes_bp = Blueprint('notes', __name__, url_prefix='/notes')

@notes_bp.route('/')
def index():
    """
    List all reading notes for the user.
    Template: notes/index.html
    """
    pass

@notes_bp.route('/new', methods=['GET'])
def new_note():
    """
    Show blank editor for a new note.
    Template: notes/edit.html
    """
    pass

@notes_bp.route('/edit/<int:id>', methods=['GET'])
def edit_note(id):
    """
    Show editor for an existing note.
    Template: notes/edit.html
    """
    pass

@notes_bp.route('/save', methods=['POST'])
def save_note():
    """
    Create or update a note.
    Inputs: id (optional), book_title, chapter, content
    Logic: Call Note.create() or Note.update().
    Output: Redirect to notes index.
    """
    pass

@notes_bp.route('/delete/<int:id>', methods=['POST'])
def delete_note(id):
    """
    Delete a note.
    Logic: Call Note.delete().
    Output: Redirect to notes index.
    """
    pass
