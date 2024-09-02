from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date, time


# Team
class TeamBase(BaseModel):
    name: Optional[str]
    image: Optional[HttpUrl]
    region: Optional[str]
    category: Optional[str]
    league: Optional[str]
    sns_accounts: Optional[dict] = {}


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass


class Team(TeamBase):
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
