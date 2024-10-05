from pydantic import BaseModel
from typing import Optional
from datetime import date, time
from enum import Enum as PyEnum


# Team
class TeamBase(BaseModel):
    name: str
    region: str
    prefecture: str
    category: str
    league: str


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    id: int


class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True


# Recruitment
class StatusEnum(str, PyEnum):
    open = "募集中"
    matched = "マッチ済み"


class RecruitmentBase(BaseModel):
    status: Optional[StatusEnum] = StatusEnum.open
    year: int
    month: int
    day: int
    start_time: str
    end_time: str
    location: str
    name: Optional[str] = None

    class Config:
        use_enum_values = True


class RecruitmentCreate(RecruitmentBase):
    pass


class RecruitmentUpdate(RecruitmentBase):
    id: int


class Recruitment(RecruitmentBase):
    id: int

    class Config:
        orm_mode = True


# Player
class PositionEnum(PyEnum):
    GK = "GK"
    DF = "DF"
    MF = "MF"
    FW = "FW"


class PlayerBase(BaseModel):
    position: PositionEnum
    number: int
    namae: str
    name: str

    class Config:
        use_enum_values = True


class PlayerCreate(PlayerBase):
    pass


class PlayerUpdate(PlayerBase):
    id: int


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
