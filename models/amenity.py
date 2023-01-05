#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.place import place_amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """ amenity class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
