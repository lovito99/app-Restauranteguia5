from sqlalchemy import Column, Integer, String, Text
from .base import Base

class TPerfil(Base):
    __tablename__ = "tperfil"

    nidtperfil = Column(Integer, primary_key=True, autoincrement=True)
    cnombre = Column(String(50), unique=True, nullable=False)
    cdescripcion = Column(Text)
