# seguridad/token.py
import jwt
from datetime import datetime, timedelta
from modelos.usuariodto import CUsuarioDTO

SECRET_KEY = "clave_super_secreta"  # usar variable de entorno

def generar_token(usuario:CUsuarioDTO):
    payload = {
        "usuario_id": usuario.nidtusaurio,
        "email": usuario.cemail,
        "exp": datetime.utcnow() + timedelta(hours=2),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def validar_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
