#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if storage_type == 'db':
        cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    else:
        @property
        def cities(self):
            '''
            '''
            cities_dict = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_dict.append(city)
            return related_cities