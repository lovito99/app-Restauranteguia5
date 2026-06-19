# servicio/usuarioservicio.py
from dao.usuariodao import UsuarioDAO
from seguridad.token import generar_token

class UsuarioServicio:
    def __init__(self):
        self.usuarioDAO = UsuarioDAO()

    def listar_usuarios(self):
        return self.usuarioDAO.listar()

    def login(self, email, password):
        usuario = self.usuarioDAO.login(email, password)
        if usuario:
            token = generar_token(usuario)
            return {"usuario": usuario, "token": token}
        return None

    def iniciarSesion(self,email,password):
        usuario = self.usuarioDAO.retornarUsuario(email)
        return usuario
