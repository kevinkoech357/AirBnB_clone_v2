#!/usr/bin/python3

"""
State Module for HBNB project
"""

from models.base_model import BaseModel, Base
from sqlaclhemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel):
    """ State class """
    # name = ""
    __tablename__ = 'states'

    # id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # For DBStorage
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
