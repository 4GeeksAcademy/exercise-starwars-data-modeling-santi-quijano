import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)


class User_Favorites(Base):
    __tablename__ = 'user_favorites'
    id = Column(Integer, primary_key=True)
    name_of_favorte = Column(String(100))
    favorite_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Star_Systems(Base):
    __tablename__ = 'star_systems'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    galactic_coordinates = Column(String(50))

class Factions(Base):
    __tablename__ = 'factions'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    leader = Column(String(100), unique=True, nullable=False)
    organization_type = Column(String(100))
    capital = Column(String(100))
    affiliation = Column(String(100))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    population = Column(Integer)
    terrain = Column(String(100))
    climate = Column(String(100))
    from_star_systems_id = Column(Integer, ForeignKey('star_systems.id'))
    star_systems = relationship(Star_Systems)
    controlling_faction_id = Column(Integer, ForeignKey('factions.id'))
    factions = relationship(Factions)

class Species(Base): 
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    classification = Column(String(100), unique=True, nullable=False)
    lifespan = Column(Integer)
    language = Column(String(100), nullable=False)

class Planet_Species(Base):
    __tablename__ = 'planet_species'
    planet_species_id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship(Species)

class Characters (Base):
    __tablename__ = 'charactes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    height = Column(Integer)
    weight = Column(Integer)
    birthdate = Column(Integer)
    gender = Column(String)
    occupation = Column(String(50))
    from_planet_Id = Column(Integer, ForeignKey('planet.id'))
    planets = relationship(Planets)
    from_faction_id = Column(Integer, ForeignKey('factions.id'))
    Factions = relationship(Factions)
    from_species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship(Species)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
