from sqlalchemy.orm import Session

from . import models, schemas


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
