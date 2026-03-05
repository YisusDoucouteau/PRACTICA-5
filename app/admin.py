from flask import redirect, url_for, request
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from wtforms.fields import PasswordField
from flask_admin.menu import MenuLink
from .extensions import db
from .models import User, Producto  # ajusta si tus modelos se llaman distinto
from flask_admin import expose
from .models import User, Producto



class AdminHome(AdminIndexView):
    @expose('/')
    def index(self):
        if not self.is_accessible():
            return self.inaccessible_callback(name='index')

        total_usuarios = User.query.count()
        total_productos = Producto.query.count()
        stock_total = db.session.query(db.func.sum(Producto.stock)).scalar() or 0
        extra_css = ["/static/admin.css"]
        extra_js = ["/static/admin.js"]
        return self.render(
            'admin/dashboard.html',
            total_usuarios=total_usuarios,
            total_productos=total_productos,
            stock_total=stock_total
        )


class BaseAdminModelView(ModelView):
    # Seguridad
    def is_accessible(self):
        return current_user.is_authenticated and getattr(current_user, "role", "") == "admin"

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login", next=request.url))

    # interfaz para el usuario 
   
    extra_css = ["/static/admin.css"]

    # traducciones
    can_create = True
    can_edit = True
    can_delete = True

    create_modal = True
    edit_modal = True
    extra_css = ["/static/admin.css"]
    extra_js = ["/static/admin.js"]
    # textos en español
    create_modal_title = "Crear registro"
    edit_modal_title = "Editar registro"
    details_modal_title = "Detalle del registro"
    
class UserAdmin(BaseAdminModelView):
    column_list = ("id", "username", "role")
    column_searchable_list = ("username", "role")
    column_filters = ("role",)
    column_sortable_list = ("id", "username", "role")
    column_labels = {
  "id": "ID",
  "username": "Usuario",
  "role": "Rol"
}
    column_exclude_list = ("password_hash",)  # según tu modelo

    form_extra_fields = {
        "password": PasswordField("Contraseña")
    }

    def on_model_change(self, form, model, is_created):
        # Si escriben password, se guarda hasheada
        if form.password.data:
            model.set_password(form.password.data)


class ProductoAdmin(BaseAdminModelView):
    column_list = ("id", "nombre", "precio", "stock")
    column_searchable_list = ("nombre",)
    column_filters = ("stock",)
    column_sortable_list = ("id", "nombre", "precio", "stock")
    column_labels = {
        "id": "ID",
        "nombre": "Nombre",
        "precio": "Precio (Bs.)",
        "stock": "Stock",
    }
    column_default_sort = ("id", True)


def init_admin(app):

    admin = Admin(
        app,
        name="Panel de Administración",
        index_view=AdminHome(url="/admin")
    )

    admin.add_view(UserAdmin(User, db.session, name="Usuarios", category="Gestión"))
    admin.add_view(ProductoAdmin(Producto, db.session, name="Productos", category="Catálogo"))

    # botón inicio
    admin.add_link(MenuLink(name="Inicio", url="/"))

    # botón logout
    admin.add_link(MenuLink(name="Cerrar sesión", url="/logout"))
    
