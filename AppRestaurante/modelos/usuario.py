from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class CUsuario(Base):
    __tablename__ = "tusuario"
    nidtusuario = Column(Integer, primary_key=True, autoincrement=True)
    nidtperfil = Column(Integer, ForeignKey("tperfil.nidtperfil"), nullable=False)
    cnombre = Column(String(100), nullable=False)
    cemail = Column(String(100), unique=True)
    cpassword = Column(String(255), nullable=False)
