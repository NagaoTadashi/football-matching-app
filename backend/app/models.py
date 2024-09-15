from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time, Enum
from sqlalchemy.orm import relationship

from .database import Base


# Team
class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True, index=True)
    region = Column(String, nullable=True)
    prefecture = Column(String, nullable=True)
    category = Column(String, nullable=True)
    league = Column(String, nullable=True)

    recruitments = relationship("Recruitment", back_populates="team")


# Recruitment
class Recruitment(Base):
    __tablename__ = "recruitments"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))
    status = Column(Enum("募集中", "マッチ済み"), default="募集中")
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    location = Column(String, nullable=False)

    team = relationship("Team", back_populates="recruitments")


# Player
class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    position = Column(String)
    number = Column(Integer)
    namae = Column(String)
    name = Column(String)


# Match
class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    opponent = Column(String)
    date = Column(Date)
    time = Column(Time)
    venue = Column(String)
    my_team_score = Column(Integer)
    opponent_score = Column(Integer)
