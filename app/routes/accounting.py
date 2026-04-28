from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.ledger import LedgerEntry

accounting_bp = Blueprint('accounting', __name__, url_prefix='/accounting')

@accounting_bp.route('/')
@login_required
def index():
    """
    Financial overview dashboard.
    """
    entries = LedgerEntry.get_all(user_id=current_user.id)
    
    total_income = sum(e.amount for e in entries if e.type == 'income')
    total_expense = sum(e.amount for e in entries if e.type == 'expense')
    balance = total_income - total_expense

    return render_template('accounting/index.html', entries=entries, balance=balance, income=total_income, expense=total_expense)

@accounting_bp.route('/add', methods=['POST'])
@login_required
def add_entry():
    """
    Record a new income or expense.
    """
    amount = request.form.get('amount', type=float)
    entry_type = request.form.get('type')
    category = request.form.get('category')
    note = request.form.get('note')
    
    if not amount or not entry_type:
        flash('Amount and Type are required!')
        return redirect(url_for('accounting.index'))

    LedgerEntry.create(user_id=current_user.id, amount=amount, type=entry_type, category=category, note=note)
    flash('Entry recorded.')
    return redirect(url_for('accounting.index'))

@accounting_bp.route('/stats')
@login_required
def stats():
    """
    Show financial trends and category charts.
    """
    # Simplified for MVP: Logic can be added here for category-wise grouping
    return render_template('accounting/stats.html')
