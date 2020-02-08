from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__,
                template_folder='../client/templates',
                static_folder='../client/static')
    app.config.from_object('app.config.DevelopmentConfig')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.main.controllers import main_bp
        from app.account.controllers import account_bp
        from app.api.controllers import api_bp
        app.register_blueprint(main_bp)
        app.register_blueprint(account_bp)
        app.register_blueprint(api_bp)

    return app