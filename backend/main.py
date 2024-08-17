from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from datetime import date, time

app = FastAPI()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Player(BaseModel):
    id: int
    position: str
    number: int
    namae: str
    name: str


class Match(BaseModel):
    id: int
    opponent: str
    date: date
    time: time
    venue: str
    my_team_score: int
    opponent_score: int


member = [
    Player(id=1, position="GK", namae="長尾 考梓", name="Tadashi Nagao", number=1),
    Player(id=2, position="GK", namae="長尾 考梓", name="Tadashi Nagao", number=2),
    Player(id=3, position="DF", namae="長尾 考梓", name="Tadashi Nagao", number=3),
    Player(id=4, position="DF", namae="長尾 考梓", name="Tadashi Nagao", number=4),
    Player(id=5, position="DF", namae="長尾 考梓", name="Tadashi Nagao", number=5),
    Player(id=6, position="DF", namae="長尾 考梓", name="Tadashi Nagao", number=6),
    Player(id=7, position="DF", namae="長尾 考梓", name="Tadashi Nagao", number=7),
    Player(id=8, position="DF", namae="長尾 考梓", name="Tadashi Nagao", number=8),
    Player(id=9, position="MF", namae="長尾 考梓", name="Tadashi Nagao", number=9),
    Player(id=10, position="MF", namae="長尾 考梓", name="Tadashi Nagao", number=10),
    Player(id=11, position="MF", namae="長尾 考梓", name="Tadashi Nagao", number=11),
    Player(id=12, position="MF", namae="長尾 考梓", name="Tadashi Nagao", number=12),
    Player(id=13, position="MF", namae="長尾 考梓", name="Tadashi Nagao", number=13),
    Player(id=14, position="MF", namae="長尾 考梓", name="Tadashi Nagao", number=14),
    Player(id=15, position="MF", namae="長尾 考梓", name="Tadashi Nagao", number=15),
    Player(id=16, position="MF", namae="長尾 考梓", name="Tadashi Nagao", number=16),
    Player(id=17, position="FW", namae="長尾 考梓", name="Tadashi Nagao", number=17),
    Player(id=18, position="FW", namae="長尾 考梓", name="Tadashi Nagao", number=18),
    Player(id=19, position="FW", namae="長尾 考梓", name="Tadashi Nagao", number=19),
    Player(id=20, position="FW", namae="長尾 考梓", name="Tadashi Nagao", number=20),
]

matches = [
    Match(
        id=1,
        opponent="Red Dragons",
        date=date(2024, 8, 10),
        time=time(15, 30),
        venue="Dragon Stadium",
        my_team_score=3,
        opponent_score=2,
    ),
    Match(
        id=2,
        opponent="Blue Eagles",
        date=date(2024, 8, 17),
        time=time(18, 0),
        venue="Eagle Arena",
        my_team_score=1,
        opponent_score=1,
    ),
    Match(
        id=3,
        opponent="Green Wolves",
        date=date(2024, 8, 24),
        time=time(13, 45),
        venue="Wolf Park",
        my_team_score=2,
        opponent_score=3,
    ),
    Match(
        id=4,
        opponent="Yellow Tigers",
        date=date(2024, 8, 31),
        time=time(16, 0),
        venue="Tiger Arena",
        my_team_score=4,
        opponent_score=0,
    ),
    Match(
        id=5,
        opponent="Black Panthers",
        date=date(2024, 9, 7),
        time=time(14, 30),
        venue="Panther Field",
        my_team_score=0,
        opponent_score=1,
    ),
    Match(
        id=6,
        opponent="White Sharks",
        date=date(2024, 9, 14),
        time=time(19, 15),
        venue="Shark Stadium",
        my_team_score=2,
        opponent_score=2,
    ),
    Match(
        id=7,
        opponent="Purple Falcons",
        date=date(2024, 9, 21),
        time=time(13, 0),
        venue="Falcon Nest",
        my_team_score=3,
        opponent_score=4,
    ),
    Match(
        id=8,
        opponent="Orange Lions",
        date=date(2024, 9, 28),
        time=time(17, 45),
        venue="Lion's Den",
        my_team_score=1,
        opponent_score=1,
    ),
    Match(
        id=9,
        opponent="Silver Foxes",
        date=date(2024, 10, 5),
        time=time(15, 0),
        venue="Fox Arena",
        my_team_score=0,
        opponent_score=3,
    ),
    Match(
        id=10,
        opponent="Bronze Bears",
        date=date(2024, 10, 12),
        time=time(18, 30),
        venue="Bear Cave",
        my_team_score=4,
        opponent_score=2,
    ),
]


@app.get("/matches", response_model=List[Match])
async def get_matches():
    return matches


@app.get("/member", response_model=List[Player])
async def get_member():
    return member
