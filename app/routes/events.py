from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.event import Event, EventRegistration

events_bp = Blueprint('events', __name__, url_prefix='/events')

@events_bp.route('/')
@login_required
def index():
    """
    List all available events.
    """
    events = Event.get_all()
    return render_template('events/index.html', events=events)

@events_bp.route('/<int:id>')
@login_required
def detail(id):
    """
    Show details for a specific event.
    """
    event = Event.get_by_id(id)
    if not event:
        flash('Event not found.')
        return redirect(url_for('events.index'))
    
    # Check if user is already registered
    is_registered = any(r.user_id == current_user.id for r in event.registrations)
    
    return render_template('events/detail.html', event=event, is_registered=is_registered)

@events_bp.route('/register/<int:id>', methods=['POST'])
@login_required
def register_event(id):
    """
    Register the logged-in user for an event.
    """
    event = Event.get_by_id(id)
    if not event:
        flash('Event not found.')
        return redirect(url_for('events.index'))

    if len(event.registrations) >= event.capacity:
        flash('Event is full!')
        return redirect(url_for('events.detail', id=id))

    registration = EventRegistration.create(user_id=current_user.id, event_id=id)
    if registration:
        flash('Registered successfully!')
    else:
        flash('You are already registered for this event.')

    return redirect(url_for('events.detail', id=id))
