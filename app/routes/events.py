from flask import Blueprint, render_template, request, redirect, url_for, flash

events_bp = Blueprint('events', __name__, url_prefix='/events')

@events_bp.route('/')
def index():
    """
    List all available events.
    Template: events/index.html
    """
    pass

@events_bp.route('/<int:id>')
def detail(id):
    """
    Show details for a specific event.
    Template: events/detail.html
    """
    pass

@events_bp.route('/register/<int:id>', methods=['POST'])
def register_event(id):
    """
    Register the logged-in user for an event.
    Logic: Call EventRegistration.create().
    Output: Redirect to event detail or index with success/error flash.
    """
    pass
