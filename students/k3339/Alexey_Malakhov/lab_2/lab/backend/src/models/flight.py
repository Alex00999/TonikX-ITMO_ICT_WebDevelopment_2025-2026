from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.models.base import Base


class Flight(Base):
    __tablename__ = "flights"

    id_flight = Column(Integer, primary_key=True)
    flight_number = Column(String(10), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    gate_number = Column(String(10), nullable=False)

    flight_type_id = Column(Integer, ForeignKey("flight_types.id_flight_type"), nullable=False)
    flight_status_id = Column(Integer, ForeignKey("flight_statuses.id_flight_status"), nullable=False)
    airline_id = Column(Integer, ForeignKey("airlines.id_airline"), nullable=False)

    # связи
    reservations = relationship("Reservation", back_populates="flight", cascade="all, delete-orphan", lazy="selectin")

    flight_type = relationship("FlightType", lazy="selectin")
    flight_status = relationship("FlightStatus", lazy="selectin")
    airline = relationship("Airlane", lazy="selectin")

    users = relationship(
        "User",
        secondary="reservations",
        primaryjoin="Flight.id_flight==Reservation.flight_id",
        secondaryjoin="User.id_user==Reservation.user_id",
        viewonly=True,
        overlaps="reservations,user,flights",
        lazy="selectin",
    )
