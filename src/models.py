import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    password = Column(String(12), nullable=False)
    is_active = Column(Boolean(), nullable=False)
    user_fav = Column(Boolean(), primary_key=True, nullable=True)

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)


class Favorites(Base):
    __tablename__ = 'Favorites'
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    user_fav = Column(Boolean(), ForeignKey('User.id'))
    Character_fav = Column(String(25), ForeignKey('Characters.id'))
    Planet_fav = Column(String(25), ForeignKey('Planets.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')