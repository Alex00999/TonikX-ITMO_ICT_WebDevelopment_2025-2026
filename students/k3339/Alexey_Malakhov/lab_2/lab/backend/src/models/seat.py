# models/seat.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base


class Seat(Base):
    __tablename__ = "seats"

    id_seat = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey("flights.id_flight", ondelete="CASCADE"), nullable=False)
    seat_number = Column(String(5), nullable=False)
    service_class = Column(String(10), nullable=False)
    is_blocked = Column(Integer, nullable=False, default=0)

    flight = relationship("Flight")
    reservations = relationship("Reservation", back_populates="seat")
