from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import relationship

from .database import Base


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    opponent = Column(String)
    date = Column(Date)
    time = Column(Time)
    venue = Column(String)
    my_team_score = Column(Integer)
    opponent_score = Column(Integer)


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    position = Column(String)
    number = Column(Integer)
    namae = Column(String)
    name = Column(String)
