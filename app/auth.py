from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from .extensions import db
from .models import User, Producto

auth_bp = Blueprint("auth", __name__, template_folder="templates")


@auth_bp.route("/")
@auth_bp.route("/index")
@login_required
def index():
    """Página principal (después de iniciar sesión)."""
    total_productos = Producto.query.count() if Producto.query else 0
    return render_template("index.html", total_productos=total_productos)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("sesión iniciada.", "success")
            return redirect(url_for("auth.index"))

        flash("❌ Usuario o contraseña incorrectos.", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash(" Sesión cerrada.", "info")
    return redirect(url_for("auth.login"))
