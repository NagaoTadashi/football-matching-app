from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time, Text, JSON
from sqlalchemy.orm import relationship

from .database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True, index=True)
    image = Column(Text, nullable=True)  # 画像URL
    region = Column(String, nullable=True)
    category = Column(String, nullable=True)
    league = Column(String, nullable=True)
    sns_accounts = Column(JSON, default={})  # SNSアカウントを辞書で保持


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
