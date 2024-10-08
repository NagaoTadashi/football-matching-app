from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas


# Team
def get_team_info(db: Session, uid: str):
    return db.query(models.Team).filter(models.Team.uid == uid).first()


def create_team_info(db: Session, team_info: schemas.TeamCreate, uid: str):
    db_team_info = models.Team(
        uid=uid,
        name=team_info.name,
        region=team_info.region,
        prefecture=team_info.prefecture,
        category=team_info.category,
        league=team_info.league,
    )

    db.add(db_team_info)
    db.commit()
    db.refresh(db_team_info)
    return db_team_info


def update_team_info(
    db: Session,
    team_id: int,
    team_info_update: schemas.TeamUpdate,
):
    team_info = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team_info:
        return None

    team_info.name = team_info_update.name
    team_info.region = team_info_update.region
    team_info.prefecture = team_info_update.prefecture
    team_info.category = team_info_update.category
    team_info.league = team_info_update.league

    db.commit()
    db.refresh(team_info)
    return team_info


# Recruitment
def get_my_team_recruitments(db: Session, uid: str):
    return db.query(models.Recruitment).filter(models.Recruitment.uid == uid).all()


def get_other_team_recruitments(db: Session, uid: str):
    stmt = (
        select(
            models.Recruitment.id,
            models.Recruitment.status,
            models.Recruitment.year,
            models.Recruitment.month,
            models.Recruitment.day,
            models.Recruitment.start_time,
            models.Recruitment.end_time,
            models.Recruitment.location,
            models.Team.name,
            models.Team.region,
            models.Team.prefecture,
            models.Team.category,
            models.Team.league,
        )
        .join(models.Team, models.Recruitment.uid == models.Team.uid)
        .filter(models.Recruitment.uid != uid)
        .filter(models.Recruitment.status == "募集中")
    )
    return db.execute(stmt).all()


def create_recruitment(db: Session, recruitment: schemas.RecruitmentCreate, uid: str):
    db_recruitment = models.Recruitment(
        uid=uid,
        status=recruitment.status,
        year=recruitment.year,
        month=recruitment.month,
        day=recruitment.day,
        start_time=recruitment.start_time,
        end_time=recruitment.end_time,
        location=recruitment.location,
    )
    db.add(db_recruitment)
    db.commit()
    db.refresh(db_recruitment)
    return db_recruitment


def update_recruitment(
    db: Session, recruitment_id: int, recruitment_update: schemas.RecruitmentUpdate
):
    recruitment = (
        db.query(models.Recruitment)
        .filter(models.Recruitment.id == recruitment_id)
        .first()
    )
    if not recruitment:
        return None

    recruitment.year = recruitment_update.year
    recruitment.month = recruitment_update.month
    recruitment.day = recruitment_update.day
    recruitment.start_time = recruitment_update.start_time
    recruitment.end_time = recruitment_update.end_time
    recruitment.location = recruitment_update.location

    db.commit()
    db.refresh(recruitment)
    return recruitment


def delete_recruitment(db: Session, recruitment_id: int):
    recruitment = (
        db.query(models.Recruitment)
        .filter(models.Recruitment.id == recruitment_id)
        .first()
    )
    if recruitment is None:
        return None

    db.delete(recruitment)
    db.commit()
    return recruitment


# Application
def get_application_requests(db: Session, uid: str):
    stmt = (
        select(
            models.Application.id,
            models.Application.recruitment_id,
            models.Recruitment.year,
            models.Recruitment.month,
            models.Recruitment.day,
            models.Recruitment.start_time,
            models.Recruitment.end_time,
            models.Recruitment.location,
            models.Team.name,
            models.Team.region,
            models.Team.prefecture,
            models.Team.category,
            models.Team.league,
        )
        .join(
            models.Application,
            models.Recruitment.id == models.Application.recruitment_id,
        )
        .join(models.Team, models.Application.uid == models.Team.uid)
        .filter(models.Recruitment.uid == uid)
    )
    return db.execute(stmt).all()


def create_application(db: Session, application: schemas.ApplicationCreate, uid: str):
    db_application = models.Application(
        recruitment_id=application.recruitment_id,
        uid=uid,
        status=application.status,
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


# Player
def get_players(db: Session, uid: str):
    return db.query(models.Player).filter(models.Player.uid == uid).all()


def create_player(db: Session, player: schemas.PlayerCreate, uid: str):
    db_player = models.Player(
        uid=uid,
        position=player.position,
        namae=player.namae,
        name=player.name,
        number=player.number,
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def update_player(db: Session, player_id: int, player_update: schemas.PlayerUpdate):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        return None

    player.position = player_update.position
    player.number = player_update.number
    player.namae = player_update.namae
    player.name = player_update.name

    db.commit()
    db.refresh(player)
    return player


def delete_player(db: Session, player_id: int):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if player is None:
        return None

    db.delete(player)
    db.commit()
    return player


# Match
def get_matches(db: Session):
    return db.query(models.Match).all()


def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(
        opponent=match.opponent,
        date=match.date,
        time=match.time,
        venue=match.venue,
        my_team_score=match.my_team_score,
        opponent_score=match.opponent_score,
    )
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match
