from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.note import Note

notes_bp = Blueprint('notes', __name__, url_prefix='/notes')

@notes_bp.route('/')
@login_required
def index():
    """
    List all reading notes for the user.
    """
    notes = Note.get_all(user_id=current_user.id)
    return render_template('notes/index.html', notes=notes)

@notes_bp.route('/new', methods=['GET'])
@login_required
def new_note():
    """
    Show blank editor for a new note.
    """
    return render_template('notes/edit.html', note=None)

@notes_bp.route('/edit/<int:id>', methods=['GET'])
@login_required
def edit_note(id):
    """
    Show editor for an existing note.
    """
    note = Note.get_by_id(id)
    if not note or note.user_id != current_user.id:
        flash('Note not found.')
        return redirect(url_for('notes.index'))
    return render_template('notes/edit.html', note=note)

@notes_bp.route('/save', methods=['POST'])
@login_required
def save_note():
    """
    Create or update a note.
    """
    note_id = request.form.get('id')
    book_title = request.form.get('book_title')
    chapter = request.form.get('chapter')
    content = request.form.get('content')
    
    if not book_title:
        flash('Book title is required!')
        return redirect(url_for('notes.index'))

    if note_id:
        note = Note.get_by_id(int(note_id))
        if note and note.user_id == current_user.id:
            note.update(book_title=book_title, chapter=chapter, content=content)
            flash('Note updated!')
    else:
        Note.create(user_id=current_user.id, book_title=book_title, chapter=chapter, content=content)
        flash('Note created!')
        
    return redirect(url_for('notes.index'))

@notes_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_note(id):
    """
    Delete a note.
    """
    note = Note.get_by_id(id)
    if not note or note.user_id != current_user.id:
        flash('Note not found.')
        return redirect(url_for('notes.index'))

    note.delete()
    flash('Note deleted.')
    return redirect(url_for('notes.index'))
