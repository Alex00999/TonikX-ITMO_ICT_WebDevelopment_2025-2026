from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.models.base import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id_ticket = Column(Integer, primary_key=True)
