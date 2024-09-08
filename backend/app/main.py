from fastapi import FastAPI, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


# Team
@app.get("/team_info/", response_model=Optional[schemas.Team])
def get_team_info(db: Session = Depends(get_db)):
    team_info = crud.get_team_info(db)
    return team_info


@app.post("/team_info/", response_model=schemas.Team)
def create_team_info(team_info: schemas.TeamCreate, db: Session = Depends(get_db)):
    created_team_info = crud.create_team_info(db, team_info=team_info)
    return created_team_info


@app.put("/team_info/", response_model=schemas.Team)
def update_team_info(
    team_info_update: schemas.TeamUpdate, db: Session = Depends(get_db)
):
    updated_team_info = crud.update_team_info(db=db, team_info_update=team_info_update)
    return updated_team_info


# Recruitment
@app.get("/recruitments/", response_model=list[schemas.Recruitment])
def get_recruitments(db: Session = Depends(get_db)):
    recruitments = crud.get_recruitments(db)
    return recruitments


@app.post("/recruitments/", response_model=schemas.Recruitment)
def create_recruitment(
    recruitment: schemas.RecruitmentCreate, db: Session = Depends(get_db)
):
    team = db.query(models.Team).filter(models.Team.id == recruitment.team_id).first()
    if not team:
        raise HTTPException(status_code=400, detail="Team not found")

    create_recruitment = crud.create_recruitment(db=db, recruitment=recruitment)
    return create_recruitment


@app.put("/recruitments/{recruitment_id}", response_model=schemas.Recruitment)
def update_recruitment(
    recruitment_id: int,
    recruitment_update: schemas.RecruitmentUpdate,
    db: Session = Depends(get_db),
):
    updated_recruitment = crud.update_recruitment(
        db=db, recruitment_id=recruitment_id, recruitment_update=recruitment_update
    )

    if updated_recruitment is None:
        raise HTTPException(status_code=404, detail="選手情報が見つかりません")
    return updated_recruitment


@app.delete("/recruitments/{recruitment_id}", response_model=schemas.Recruitment)
def delete_recruitment(recruitment_id: int, db: Session = Depends(get_db)):
    deleted_recruitment = crud.delete_recruitment(db=db, recruitment_id=recruitment_id)

    if deleted_recruitment is None:
        raise HTTPException(status_code=404, detail="選手情報が見つかりません")
    return deleted_recruitment


# Player
@app.get("/players/", response_model=list[schemas.Player])
def get_players(db: Session = Depends(get_db)):
    players = crud.get_players(db)
    return players


@app.post("/players/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    created_player = crud.create_player(db=db, player=player)
    return created_player


@app.put("/players/{player_id}", response_model=schemas.Player)
def update_player(
    player_id: int, player_update: schemas.PlayerUpdate, db: Session = Depends(get_db)
):
    updated_player = crud.update_player(
        db=db, player_id=player_id, player_update=player_update
    )

    if updated_player is None:
        raise HTTPException(status_code=404, detail="選手情報が見つかりません")
    return updated_player


@app.delete("/players/{player_id}", response_model=schemas.Player)
def delete_player(player_id: int, db: Session = Depends(get_db)):
    deleted_player = crud.delete_player(db=db, player_id=player_id)

    if deleted_player is None:
        raise HTTPException(status_code=404, detail="選手情報が見つかりません")
    return deleted_player


# Match
@app.get("/matches/", response_model=list[schemas.Match])
def get_matches(db: Session = Depends(get_db)):
    matches = crud.get_matches(db)
    return matches


# @app.post("/match/", response_model=schemas.Match)
# def create_match(match: schemas.MatchCreate, db: Session = Depends(get_db)):
#     created_match = crud.create_match(db=db, match=match)
#     return created_match
