from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


class Player(BaseModel):
    id: int
    position: str
    number: int
    namae: str
    name: str


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


@app.get("/member", response_model=List[Player])
async def get_players():
    return member
