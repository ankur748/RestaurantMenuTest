from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id              = Column(Integer, primary_key = True)
    name            = Column(String(200), nullable = False)
    email           = Column(String(200), nullable = False)
    picture         = Column(String(200))

class Restaurant(Base):
    __tablename__ = "restaurants"

    id              = Column(Integer, primary_key = True)
    name            = Column(String(200), nullable = False)
    user_id         = Column(Integer, ForeignKey('users.id'))
    user            = relationship(User)

class MenuItem(Base):
    __tablename__ = "menu_items"

    id              = Column(Integer, primary_key = True)
    name            = Column(String(200), nullable = False)
    description     = Column(String(200))
    price           = Column(String(8), nullable = False)
    course          = Column(String(200))
    restaurant_id   = Column(Integer, ForeignKey('restaurants.id'))
    restaurant      = relationship(Restaurant)
    user_id         = Column(Integer, ForeignKey('users.id'))
    user            = relationship(User)

engine = create_engine('sqlite:///RestaurantMenu.db')
Base.metadata.create_all(engine)