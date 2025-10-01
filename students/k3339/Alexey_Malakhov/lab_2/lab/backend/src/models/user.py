from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.models.base import Base


class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True)
    last_name = Column(String(40), nullable=False)
    first_name = Column(String(40), nullable=False)
    patronymic = Column(String(40), nullable=True)
    passport_number = Column(String(20), nullable=False)
