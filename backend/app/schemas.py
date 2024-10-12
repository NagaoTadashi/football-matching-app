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
class RecruitmentStatusEnum(str, PyEnum):
    open = "募集中"
    waiting_for_response = "申し込み受領"
    matched = "マッチ済み"


class RecruitmentBase(BaseModel):
    status: Optional[RecruitmentStatusEnum] = RecruitmentStatusEnum.open
    year: int
    month: int
    day: int
    start_time: str
    end_time: str
    location: str

    class Config:
        use_enum_values = True


class RecruitmentCreate(RecruitmentBase):
    pass


class Recruitment(RecruitmentBase):
    id: int

    class Config:
        orm_mode = True


class OtherTeamRecruitment(RecruitmentBase):
    id: int
    name: str
    region: str
    prefecture: str
    category: str
    league: str

    class Config:
        orm_mode = True


# Application
class ApplicationStatusEnum(str, PyEnum):
    waiting_for_response = "回答待ち"
    approved = "承認"
    decline = "辞退"


class ApplicationBase(BaseModel):
    recruitment_id: int
    status: Optional[ApplicationStatusEnum] = ApplicationStatusEnum.waiting_for_response

    class Config:
        use_enum_values = True


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(ApplicationBase):
    id: int


class Application(ApplicationBase):
    id: int

    class Config:
        orm_mode = True


class ApplicationRequest(ApplicationBase, TeamBase, RecruitmentBase):
    id: int

    class Config:
        orm_mode = True


class ApplicationStatus(ApplicationBase, TeamBase, RecruitmentBase):
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
    height: int
    weight: int
    previous_team: str

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
