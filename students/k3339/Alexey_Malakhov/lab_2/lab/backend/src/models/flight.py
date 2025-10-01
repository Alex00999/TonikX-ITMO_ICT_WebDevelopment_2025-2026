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
