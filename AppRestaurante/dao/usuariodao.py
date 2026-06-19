# usuario_repository.py
from dao.Conexion import Conexion
from modelos.usuario import  CUsuario
from modelos.usuariodto import CUsuarioDTO


class UsuarioDAO:
    def __init__(self):
        self.conexion = Conexion()

    def listar(self):
        self.conexion.abrir()
        cursor = self.conexion.get_cursor()
        cursor.execute("CALL sp_listar_tusuario()")
        filas = cursor.fetchall()
        self.conexion.cerrar()
        usuarios = [CUsuario(
            nidtusuario=fila["nidtusuario"],
            nidtperfil=fila["nidtperfil"],
            cnombre=fila["cnombre"],
            cemail=fila["cemail"],
            cpassword=""
        ) for fila in filas]
        return usuarios

    def login(self, email, password):
        self.conexion.abrir()
        cursor = self.conexion.get_cursor()
        cursor.execute("CALL sp_iniciar_sesion(%s, %s)", (email, password))
        fila=cursor.fetchall()
        self.conexion.cerrar()
        usuarioDTO = CUsuarioDTO(fila[0]["estado"],
                                 fila[0]["cemail"],
                                 fila[0]["nidtusuario"],
                                 fila[0]["nidtperfil"],
                                 fila[0]["cnombre"])
        return usuarioDTO

    def retornarUsuario(self,email):
        self.conexion.abrir()
        cursor = self.conexion.get_cursor()
        cursor.execute("CALL sp_retornar_usuario(%s, %s)", (email))
        fila = cursor.fetchall()
        self.conexion.cerrar()
        usuario=CUsuario(fila[0]["nidtusuario"],
                         fila[0]["nidtperfil"],
                         fila[0]["cnombre"],
                         fila[0]["cemail"],
                         fila[0]["cpassword"])
        return usuario