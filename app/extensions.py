from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Extensiones (se inicializan en create_app)
db = SQLAlchemy()
login_manager = LoginManager()

# Nota: en versiones recientes de Flask-Admin ya no existe 'template_mode'.
# Por eso NO lo pasamos como parámetro.
admin = Admin(name="Panel de Administración")
migrate = Migrate()


def init_extensions(app):
    """Inicializa extensiones con la app."""
    db.init_app(app)

    login_manager.init_app(app)
    # El login está dentro del blueprint "auth", por eso el endpoint es "auth.login".
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Por favor inicia sesión para continuar."
    # Flask-Migrate (Alembic)
    migrate.init_app(app, db)
