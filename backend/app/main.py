from fastapi import FastAPI, Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import firebase_admin
from firebase_admin import auth, credentials, initialize_app


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

# firebase settings
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


# Firebaseトークンの検証関数
async def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(status_code=403, detail="Authorization header missing")

    token = auth_header.split(" ")[1]
    try:
        # Firebaseのトークンを検証
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=403, detail="Invalid token")


# endpoint functions


# Match
@app.get("/matches/", response_model=list[schemas.Match])
def get_matches(db: Session = Depends(get_db), user=Depends(get_current_user)):
    uid = user["uid"]
    matches = crud.get_matches(db=db, uid=uid)
    return matches


# Team
@app.get("/team_info/", response_model=Optional[schemas.Team])
def get_team_info(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    team_info = crud.get_team_info(db=db, uid=uid)
    return team_info


@app.post("/team_info/", response_model=schemas.Team)
def create_team_info(
    team_info: schemas.TeamCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    created_team_info = crud.create_team_info(db=db, team_info=team_info, uid=uid)
    return created_team_info


@app.put("/team_info/{team_id}", response_model=schemas.Team)
def update_team_info(
    team_id: int, team_info_update: schemas.TeamUpdate, db: Session = Depends(get_db)
):
    updated_team_info = crud.update_team_info(
        db=db, team_id=team_id, team_info_update=team_info_update
    )
    return updated_team_info


# Player
@app.get("/players/", response_model=list[schemas.Player])
def get_players(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    players = crud.get_players(db=db, uid=uid)
    return players


@app.post("/players/", response_model=schemas.Player)
def create_player(
    player: schemas.PlayerCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    created_player = crud.create_player(db=db, player=player, uid=uid)
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


# Recruitment
@app.get("/my_team_recruitments/", response_model=list[schemas.Recruitment])
def get_my_team_recruitments(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    recruitments = crud.get_my_team_recruitments(db=db, uid=uid)
    return recruitments


@app.get("/other_team_recruitments/", response_model=list[schemas.OtherTeamRecruitment])
def get_other_team_recruitments(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    recruitments = crud.get_other_team_recruitments(db=db, uid=uid)
    return recruitments


@app.post("/recruitments/", response_model=schemas.Recruitment)
def create_recruitment(
    recruitment: schemas.RecruitmentCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    created_recruitment = crud.create_recruitment(
        db=db, recruitment=recruitment, uid=uid
    )
    return created_recruitment


@app.delete("/recruitments/{recruitment_id}", response_model=schemas.Recruitment)
def delete_recruitment(recruitment_id: int, db: Session = Depends(get_db)):
    deleted_recruitment = crud.delete_recruitment(db=db, recruitment_id=recruitment_id)

    if deleted_recruitment is None:
        raise HTTPException(status_code=404, detail="募集投稿が見つかりません")
    return deleted_recruitment


# Application
@app.get("/application_requests/", response_model=list[schemas.ApplicationRequest])
def get_application_requests(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    application_requests = crud.get_application_requests(db=db, uid=uid)
    return application_requests


@app.post(
    "/decline_application_request/{application_id}", response_model=schemas.Application
)
def decline_application_request(application_id: int, db: Session = Depends(get_db)):
    declined_application_request = crud.decline_application_request(
        db=db, application_id=application_id
    )
    return declined_application_request


@app.get("/application_status/", response_model=list[schemas.ApplicationStatus])
def get_application_status(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    application_status = crud.get_application_status(db=db, uid=uid)
    return application_status


@app.post("/application/", response_model=schemas.Application)
def create_application(
    application: schemas.ApplicationCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    uid = user["uid"]
    created_application = crud.create_application(
        db=db, application=application, uid=uid
    )
    return created_application


@app.delete("/application/{application_id}", response_model=schemas.Application)
def delete_application(application_id: int, db: Session = Depends(get_db)):
    deleted_application = crud.delete_application(db=db, application_id=application_id)

    if deleted_application is None:
        raise HTTPException(status_code=404, detail="申し込み情報が見つかりません")
    return deleted_application
