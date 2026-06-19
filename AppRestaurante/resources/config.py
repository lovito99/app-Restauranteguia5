# config.py
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "bdrestaurante"),
    "port": int(os.getenv("DB_PORT", "3307"))
}

SECRET_KEY = os.getenv("SECRET_KEY", "clave_super_secreta")
