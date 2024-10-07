from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time, Enum
from sqlalchemy.orm import relationship

from .database import Base


# Team
class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String)
    name = Column(String)
    region = Column(String)
    prefecture = Column(String)
    category = Column(String)
    league = Column(String)


# Player
class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    uid = Column(String)
    position = Column(Enum("GK", "DF", "MF", "FW"))
    number = Column(Integer)
    namae = Column(String)
    name = Column(String)


# Recruitment
class Recruitment(Base):
    __tablename__ = "recruitments"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String)
    status = Column(Enum("募集中", "申し込み中", "終了"), default="募集中")
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    start_time = Column(String)
    end_time = Column(String)
    location = Column(String)


# Application
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    recruitment_id = Column(Integer, ForeignKey("recruitments.id"))
    uid = Column(String)
    status = Column(Enum("未回答", "承認", "拒否"), default="未回答")


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
