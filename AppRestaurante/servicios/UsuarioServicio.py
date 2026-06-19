# servicio/usuarioservicio.py
from dao.usuariodao import UsuarioDAO
from seguridad.token import generar_token
from modelos.usuariodto import CUsuarioDTO
import bcrypt

class UsuarioServicio:
    def __init__(self):
        self.usuarioDAO = UsuarioDAO()

    def listar_usuarios(self):
        return self.usuarioDAO.listar()

    def login(self, email, password):
        """
        Actividad 2: Validación centrada en el backend.
        Se busca al usuario por email y se valida el password
        en Python con bcrypt, sin depender de un SP en la BD.
        """
        usuario = self.usuarioDAO.buscar_por_email(email)
        if not usuario:
            return None

        # Verificar password con bcrypt en el backend
        if not bcrypt.checkpw(password.encode("utf-8"),
                              usuario.cpassword.encode("utf-8")):
            return None

        # Construir DTO sin exponer el password
        usuarioDTO = CUsuarioDTO(
            cestado="activo",
            nidtusaurio=usuario.nidtusuario,
            cemail=usuario.cemail,
            nidtperfil=usuario.nidtperfil,
            cnombre=usuario.cnombre
        )
        token = generar_token(usuarioDTO)
        return {"usuario": usuarioDTO, "token": token}

    def iniciarSesion(self,email,password):
        usuario = self.usuarioDAO.retornarUsuario(email)
        return usuario

    def registrar_usuario(self, email, password_hash, nombre, nidtperfil):
        """Registra un usuario con el password ya hasheado."""
        return self.usuarioDAO.registrar(email, password_hash, nombre, nidtperfil)
