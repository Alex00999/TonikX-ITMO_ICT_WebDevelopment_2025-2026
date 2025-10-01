from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.models.base import Base


class Review(Base):
    __tablename__ = "reviews"

    id_review = Column(Integer, primary_key=True)
