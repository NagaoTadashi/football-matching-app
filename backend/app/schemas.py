from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date, time


# Team
class TeamBase(BaseModel):
    name: Optional[str]
    region: Optional[str]
    prefecture: Optional[str]
    category: Optional[str]
    league: Optional[str]


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass


class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True


# Recruitment
class RecruitmentBase(BaseModel):
    location: str
    date: date
    start_time: time
    end_time: time
    status: Optional[str] = "open"


class RecruitmentCreate(RecruitmentBase):
    team_id: int


class Recruitment(RecruitmentBase):
    id: int
    team_id: int

    class Config:
        orm_mode = True


# Player
class PlayerBase(BaseModel):
    position: str
    number: int
    namae: str
    name: str


class PlayerCreate(PlayerBase):
    pass


class PlayerUpdate(PlayerBase):
    pass


class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True


# Match
class MatchBase(BaseModel):
    opponent: str
    date: date
    time: time
    venue: str
    my_team_score: Optional[int]
    opponent_score: Optional[int]


class MatchCreate(MatchBase):
    pass


class Match(MatchBase):
    id: int

    class Config:
        orm_mode = True
