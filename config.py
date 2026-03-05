import os


class Config:
    """Configuración básica.

    - Por defecto usa SQLite (para que corra "out of the box").
    - Si estás en Laragon/MySQL, define DATABASE_URL.
      Ejemplo (PyMySQL): mysql+pymysql://root:@127.0.0.1:3306/reposteria
    """

    SECRET_KEY = os.environ.get("SECRET_KEY", "una_clave_secreta")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///reposteria.db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
