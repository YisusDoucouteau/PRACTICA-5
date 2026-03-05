"""Punto de arranque (modo desarrollo).

✅ TAREA (Práctica):
1) Arreglar error de Flask-Admin (template_mode) -> SOLUCIONADO en app/extensions.py
2) Integrar Flask-Migrate y crear una tabla con migraciones -> modelo Producto en app/models.py

COMANDOS RECOMENDADOS (solo la primera vez):
  pip install -r requirements.txt
  flask db init
  flask db migrate -m "Inicial"
  flask db upgrade

EJECUTAR:
  python run.py
"""

from app import create_app
from app.extensions import db
from app.models import User

app = create_app()


def crear_admin_por_defecto():
    """Crea un usuario admin si no existe."""
    # OJO: si NO ejecutaste migraciones, las tablas no existirán.
    if not User.query.filter_by(username="admin").first():
        usuario = User(username="admin", role="admin")
        usuario.set_password("1234")
        db.session.add(usuario)
        db.session.commit()
        print("[OK] Admin creado: admin / 1234")


if __name__ == "__main__":
    with app.app_context():
        try:
            crear_admin_por_defecto()
        except Exception as e:
            print("[WARN] Aún no existe la base de datos o faltó ejecutar migraciones.")
            print("       Ejecuta: flask db migrate && flask db upgrade")
            print("       Detalle:", e)

    app.run(debug=True)
