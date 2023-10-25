#!/usr/bin/python3

"""
State Module for HBNB project
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    # name = ""
    __tablename__ = 'states'

    # id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # For DBStorage
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """
            This method returns the list of City objects
            from storage linked to the current State
            """
            from models import storage
            from models.city import City

            cities = storage.all(City)
            keys = cities.keys()
            temp = []
            for key in keys:
                if cities[key].state_id == self.id:
                    temp.append(cities[key])
            return temp
