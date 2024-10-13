from sqlalchemy import select, or_
from sqlalchemy.orm import Session, aliased

from . import models, schemas


# Match
def get_matches(db: Session, uid: str):

    home_team = aliased(models.Team)
    away_team = aliased(models.Team)

    stmt = (
        select(
            models.Match.id,
            home_team.id.label("home_team_id"),
            home_team.name.label("home_team_name"),
            home_team.region.label("home_team_region"),
            home_team.prefecture.label("home_team_prefecture"),
            home_team.category.label("home_team_category"),
            home_team.league.label("home_team_league"),
            away_team.id.label("away_team_id"),
            away_team.name.label("away_team_name"),
            away_team.region.label("away_team_region"),
            away_team.prefecture.label("away_team_prefecture"),
            away_team.category.label("away_team_category"),
            away_team.league.label("away_team_league"),
            models.Match.year,
            models.Match.month,
            models.Match.day,
            models.Match.start_time,
            models.Match.end_time,
            models.Match.location,
        )
        .select_from(models.Match)
        .join(home_team, models.Match.home_team_uid == home_team.uid)
        .join(away_team, models.Match.away_team_uid == away_team.uid)
        # .outerjoin(
        #     models.MatchRecord,
        #     and_(
        #         models.MatchRecord.match_id == models.Match.id,
        #         models.MatchRecord.uid == uid,
        #     ),
        # )
        .filter(or_(home_team.uid == uid, away_team.uid == uid))
    )
    return db.execute(stmt).all()


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


# Player
def get_players(db: Session, uid: str):
    return db.query(models.Player).filter(models.Player.uid == uid).all()


def create_player(db: Session, player: schemas.PlayerCreate, uid: str):
    db_player = models.Player(
        uid=uid,
        position=player.position,
        number=player.number,
        namae=player.namae,
        name=player.name,
        height=player.height,
        weight=player.weight,
        previous_team=player.previous_team,
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
    player.height = player_update.height
    player.weight = player_update.weight
    player.previous_team = player_update.previous_team

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


def delete_recruitment(db: Session, recruitment_id: int):
    recruitment = (
        db.query(models.Recruitment)
        .filter(models.Recruitment.id == recruitment_id)
        .first()
    )
    if recruitment is None:
        return None

    # その募集に関連する申し込みを全て取得し削除
    applications = (
        db.query(models.Application)
        .filter(models.Application.recruitment_id == recruitment_id)
        .all()
    )

    for application in applications:
        db.delete(application)

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
        .filter(models.Application.status == "回答待ち")
    )
    return db.execute(stmt).all()


def approve_application_request(db: Session, application_id: int):

    application = (
        db.query(models.Application)
        .filter(models.Application.id == application_id)
        .first()
    )
    if application is None:
        return None

    application.status = "承認"

    db_recruitment = (
        db.query(models.Recruitment)
        .filter(models.Recruitment.id == application.recruitment_id)
        .first()
    )

    if db_recruitment:
        db_recruitment.status = "マッチ済み"

    # 試合を作成
    db_match = models.Match(
        home_team_uid=db_recruitment.uid,
        away_team_uid=application.uid,
        year=db_recruitment.year,
        month=db_recruitment.month,
        day=db_recruitment.day,
        start_time=db_recruitment.start_time,
        end_time=db_recruitment.end_time,
        location=db_recruitment.location,
    )

    db.add(db_match)
    db.commit()
    db.refresh(db_match)

    db.commit()
    db.refresh(application)

    return application


def decline_application_request(db: Session, application_id: int):

    application = (
        db.query(models.Application)
        .filter(models.Application.id == application_id)
        .first()
    )
    if application is None:
        return None

    application.status = "辞退"

    db_recruitment = (
        db.query(models.Recruitment)
        .filter(models.Recruitment.id == application.recruitment_id)
        .first()
    )
    if db_recruitment:
        db_recruitment.status = "募集中"

    db.commit()
    db.refresh(application)
    return application


def get_application_status(db: Session, uid: str):
    stmt = (
        select(
            models.Application.id,
            models.Application.recruitment_id,
            models.Application.status,
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
        .join(models.Team, models.Recruitment.uid == models.Team.uid)
        .filter(models.Application.uid == uid)
    )
    return db.execute(stmt).all()


def create_application(db: Session, application: schemas.ApplicationCreate, uid: str):
    db_application = models.Application(
        recruitment_id=application.recruitment_id,
        uid=uid,
        status=application.status,
    )
    db.add(db_application)

    # 申し込みされた募集のステータスを変更
    db_recruitment = (
        db.query(models.Recruitment)
        .filter(models.Recruitment.id == application.recruitment_id)
        .first()
    )
    if not db_recruitment or db_recruitment.status != "募集中":
        return None

    db_recruitment.status = "申し込み受領"
    db.commit()
    db.refresh(db_recruitment)

    db.commit()
    db.refresh(db_application)
    return db_application


def delete_application(db: Session, application_id: int):
    application = (
        db.query(models.Application)
        .filter(models.Application.id == application_id)
        .first()
    )
    if application is None:
        return None

    # キャンセルされた募集のステータスを変更
    db_recruitment = (
        db.query(models.Recruitment)
        .filter(models.Recruitment.id == application.recruitment_id)
        .first()
    )
    if db_recruitment:
        db_recruitment.status = "募集中"
        db.commit()
        db.refresh(db_recruitment)

    db.delete(application)
    db.commit()
    return application
