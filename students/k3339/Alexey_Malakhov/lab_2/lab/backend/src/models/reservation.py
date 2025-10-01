from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.models.base import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id_reservation = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id_user"), nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.id_flight"), nullable=False)
    seat_id = Column(Integer, ForeignKey("seats.id_seat"), nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.id_flight"), nullable=False)
