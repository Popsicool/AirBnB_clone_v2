
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base




all_classes = [State, City, User, Place, Review, Amenity]
class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                           HBNB_MYSQL_USER,
                                           HBNB_MYSQL_PWD,
                                           HBNB_MYSQL_HOST,
                                           HBNB_MYSQL_DB
                                       ), pool_pre_ping=True)
        if (HBNB_ENV == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        all_objs = {}
        if cls:
            objs = self.__session.query(cls).all()
            for i in objs:
                key = i.__class__.__name__ + '.' + i.id
                all_objs[key] = i
        else:
            for c in all_classes:
                objs = self.__session.query(c).all()
                for i in objs:
                    key = i.__class__.__name__ + '.' + i.id
                    dct[key] = i


        return all_objs
    
    def new(self, obj):
        """
        """
        self.__session.add(obj)

    def save(self):
        """
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """
        """
        self.__session.close()
