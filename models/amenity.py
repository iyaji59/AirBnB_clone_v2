#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class Amenity(BaseModel, Base):
    """Representation of Amenity"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)