from sqlalchemy.orm import Session

from . import models, schemas


# Team
def get_team_info(db: Session):
    return db.query(models.Team).one()


def create_team_info(db: Session, team_info: schemas.TeamCreate):
    db_team_info = models.Team(
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
    team_info_update: schemas.TeamUpdate,
):
    team_info = db.query(models.Team).one()
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
def get_recruitments(db: Session):
    return db.query(models.Recruitment).all()


def create_recruitment(db: Session, recruitment: schemas.RecruitmentCreate):
    db_recruitment = models.Recruitment(
        team_id=recruitment.team_id,
        location=recruitment.location,
        date=recruitment.date,
        start_time=recruitment.start_time,
        end_time=recruitment.end_time,
        status=recruitment.status,
    )
    db.add(db_recruitment)
    db.commit()
    db.refresh(db_recruitment)
    return db_recruitment


# Player
def get_players(db: Session):
    return db.query(models.Player).all()


def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(
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
