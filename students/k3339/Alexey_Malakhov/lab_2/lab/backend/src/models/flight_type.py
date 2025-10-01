from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.models.base import Base


class FlightType(Base):
    __tablename__ = "flight_types"

    id_flight_type = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
