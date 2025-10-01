from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.models.base import Base


class Seat(Base):
    __tablename__ = "seats"

    id_seat = Column(Integer, primary_key=True)
    seat_number = Column(String(10), nullable=False)
    class_type = Column(String(50), nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.id_flight"), nullable=False)
