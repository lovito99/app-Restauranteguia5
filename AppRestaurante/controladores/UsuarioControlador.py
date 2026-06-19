from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from servicios.UsuarioServicio import UsuarioServicio

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


# --- ENDPOINTS / RUTAS ---

@router.post("/login", status_code=status.HTTP_200_OK)
def login(datos: LoginRequest):
    """
    Endpoint para autenticar usuarios del restaurante.
    Recibe el email y password, y retorna el objeto usuario junto con su JWT.
    """
    # Llamamos a tu servicio pasándole los datos ya validados por Pydantic
    resultado = usuario_servicio.login(datos.email, datos.password)

    # Si las credenciales fallan o el usuario no existe, tu servicio retorna None
    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El correo electrónico o la contraseña son incorrectos."
        )

    # Si todo sale bien, retorna automáticamente el dict {"usuario": ..., "token": ...} con un código 200
    return resultado


@router.get("/", status_code=status.HTTP_200_OK)
def listar():
    """
    Endpoint para listar todos los usuarios (útil para administración).
    """
    return usuario_servicio.listar_usuarios()