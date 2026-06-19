from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from servicios.UsuarioServicio import UsuarioServicio
import bcrypt

# Creamos el router para agrupar las rutas de usuario
router = APIRouter(
    prefix="/api/usuarios",
    tags=["Usuarios"]
)

# Instanciamos el servicio que ya tienes programado
usuario_servicio = UsuarioServicio()


# --- MODELOS DE PETICIÓN (Pydantic) ---
# Esto valida de forma automática lo que React envía en el cuerpo (body) del JSON
class LoginRequest(BaseModel):
    email: EmailStr  # Valida automáticamente que sea un formato de correo válido
    password: str


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    nombre: str
    nidtperfil: int


# --- ENDPOINTS / RUTAS ---

@router.post("/login", status_code=status.HTTP_200_OK)
def login(datos: LoginRequest):
    """
    Endpoint para autenticar usuarios del restaurante.
    Actividad 2: La validación del password se realiza en el backend
    con bcrypt, ya no en la base de datos.
    """
    resultado = usuario_servicio.login(datos.email, datos.password)

    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El correo electrónico o la contraseña son incorrectos."
        )

    # Serializar el DTO a dict para la respuesta JSON
    usuario = resultado["usuario"]
    return {
        "usuario": {
            "cestado": usuario.cestado,
            "nidtusuario": usuario.nidtusaurio,
            "cemail": usuario.cemail,
            "nidtperfil": usuario.nidtperfil,
            "cnombre": usuario.cnombre,
        },
        "token": resultado["token"]
    }


@router.post("/registrar", status_code=status.HTTP_201_CREATED)
def registrar(datos: RegisterRequest):
    """
    Endpoint para registrar un usuario con password hasheado (bcrypt).
    El hash se genera en el backend antes de guardar en la BD.
    """
    hashed = bcrypt.hashpw(datos.password.encode("utf-8"), bcrypt.gensalt())
    resultado = usuario_servicio.registrar_usuario(
        email=datos.email,
        password_hash=hashed.decode("utf-8"),
        nombre=datos.nombre,
        nidtperfil=datos.nidtperfil
    )
    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo registrar el usuario. Verifique que el email no esté en uso."
        )
    return {"mensaje": "Usuario registrado correctamente"}


@router.get("/", status_code=status.HTTP_200_OK)
def listar():
    """
    Endpoint para listar todos los usuarios (útil para administración).
    """
    return usuario_servicio.listar_usuarios()