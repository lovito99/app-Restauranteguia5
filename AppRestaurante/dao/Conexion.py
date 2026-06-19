import mysql.connector
from mysql.connector import Error
from resources.config import DB_CONFIG

class Conexion:
    def __init__(self, config=DB_CONFIG):
        self.config = config
        self.connection = None

    def abrir(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            print("Conexión establecida")
        except Error as e:
            print(f"Error al conectar: {e}")

    def cerrar(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    def get_cursor(self):
        if self.connection and self.connection.is_connected():
            return self.connection.cursor(dictionary=True)
        else:
            raise Exception("La conexión no está abierta")
