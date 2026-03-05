from flask import Flask
from config import Config
from .extensions import init_extensions
from .auth import auth_bp
from .admin import init_admin   # solo uno

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 1) extensiones (db, login, migrate)
    init_extensions(app)

    # 2) blueprints
    app.register_blueprint(auth_bp)

    # 3) admin (una sola vez)
    init_admin(app)

    return app