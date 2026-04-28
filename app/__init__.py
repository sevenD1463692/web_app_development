import os
from flask import Flask
from app.extensions import db
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///mylife.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Extensions
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    from app.routes.accounting import accounting_bp
    from app.routes.notes import notes_bp
    from app.routes.events import events_bp
    from app.routes.recipes import recipes_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(accounting_bp)
    app.register_blueprint(notes_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(recipes_bp)

    # Base route
    @app.route('/')
    def index():
        return "Welcome to MyLife System. Foundation is ready."

    return app

def init_db():
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database initialized.")
