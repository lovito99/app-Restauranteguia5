# main.py
from dao.Conexion import Conexion
from dao.usuariodao import UsuarioDAO

# inyección de dependencias

usuarioDAO = UsuarioDAO()

# listar usuarios
usuarios = usuarioDAO.listar()
print("Usuarios:", usuarios)
# login
resultado = usuarioDAO.login("julio@restaurante.com", "clave123")
print("Login:", resultado)
