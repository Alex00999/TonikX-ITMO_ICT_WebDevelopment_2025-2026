# models/reservation.py
from sqlalchemy import Column, ForeignKey, Integer, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from src.models.base import Base


class Reservation(Base):
    __tablename__ = "reservations"
    __table_args__ = (UniqueConstraint("flight_id", "seat_id", name="uq_resv_flight_seat"),)

    id_reservation = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id_user", ondelete="CASCADE"), nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.id_flight", ondelete="CASCADE"), nullable=False)
    seat_id = Column(Integer, ForeignKey("seats.id_seat", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime)
    canceled_at = Column(DateTime)

    user = relationship("User", back_populates="reservations", overlaps="flights,users")
    flight = relationship("Flight", back_populates="reservations", overlaps="flights,users")
    seat = relationship("Seat", back_populates="reservations")
