from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.base import Base
from .reservation import Reservation


class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, nullable=False)

    reservations = relationship("Reservation", back_populates="user", cascade="all, delete-orphan")

    flights = relationship(
        "Flight",
        secondary="reservations",
        primaryjoin="User.id_user==Reservation.user_id",
        secondaryjoin="Flight.id_flight==Reservation.flight_id",
        viewonly=True,
        overlaps="reservations,user,flights",
    )
