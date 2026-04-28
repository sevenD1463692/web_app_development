from flask import Blueprint, render_template, request, redirect, url_for, flash

accounting_bp = Blueprint('accounting', __name__, url_prefix='/accounting')

@accounting_bp.route('/')
def index():
    """
    Financial overview dashboard.
    Template: accounting/index.html
    Logic: Calculate balance and list recent entries.
    """
    pass

@accounting_bp.route('/add', methods=['POST'])
def add_entry():
    """
    Record a new income or expense.
    Inputs: amount, type, category, entry_date, note
    Logic: Call LedgerEntry.create().
    Output: Redirect to accounting index.
    """
    pass

@accounting_bp.route('/stats')
def stats():
    """
    Show financial trends and category charts.
    Template: accounting/stats.html
    """
    pass
