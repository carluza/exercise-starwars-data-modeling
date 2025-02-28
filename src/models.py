import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    climate = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    residents = relationship("People", back_populates="homeworld")

class People(Base):
    __tablename__ = 'peoples'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=False)
    homeworld = relationship("Planet", back_populates="residents")
    vehicles = relationship("Vehicle", back_populates="pilot")

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    passengers = Column(Integer, nullable=False)
    pilot_id = Column(Integer, ForeignKey("peoples.id"), nullable=False)
    pilot = relationship("People", back_populates="vehicles")

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')
