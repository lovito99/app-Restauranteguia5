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

    def buscar_por_email(self, email):
        """Busca un usuario por email sin validar password en la BD."""
        self.conexion.abrir()
        cursor = self.conexion.get_cursor()
        cursor.execute(
            "SELECT nidtusuario, nidtperfil, cnombre, cemail, cpassword "
            "FROM tusuario WHERE cemail = %s",
            (email,)
        )
        fila = cursor.fetchone()
        self.conexion.cerrar()
        if not fila:
            return None
        return CUsuario(
            nidtusuario=fila["nidtusuario"],
            nidtperfil=fila["nidtperfil"],
            cnombre=fila["cnombre"],
            cemail=fila["cemail"],
            cpassword=fila["cpassword"]
        )

    def retornarUsuario(self,email):
        self.conexion.abrir()
        cursor = self.conexion.get_cursor()
        cursor.execute("CALL sp_retornar_usuario(%s)", (email,))
        fila = cursor.fetchall()
        self.conexion.cerrar()
        usuario=CUsuario(fila[0]["nidtusuario"],
                         fila[0]["nidtperfil"],
                         fila[0]["cnombre"],
                         fila[0]["cemail"],
                         fila[0]["cpassword"])
        return usuario

    def registrar(self, email, password_hash, nombre, nidtperfil):
        """Inserta un usuario con password hasheado en la BD."""
        try:
            self.conexion.abrir()
            cursor = self.conexion.get_cursor()
            cursor.execute(
                "INSERT INTO tusuario (nidtperfil, cnombre, cemail, cpassword) "
                "VALUES (%s, %s, %s, %s)",
                (nidtperfil, nombre, email, password_hash)
            )
            self.conexion.connection.commit()
            self.conexion.cerrar()
            return True
        except Exception:
            self.conexion.cerrar()
            return False