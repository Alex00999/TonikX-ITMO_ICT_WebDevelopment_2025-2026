from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.models.base import Base


class FlightStatus(Base):
    __tablename__ = "flight_statuses"

    id_flight_status = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
