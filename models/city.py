#!/usr/bin/python3

"""
City Module for HBNB project
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.state import State

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    #  state_id = ""
    # name = ""
    __tablename__ = 'cities'

    # id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
