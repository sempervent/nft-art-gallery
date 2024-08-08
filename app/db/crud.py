from sqlalchemy.orm import Session
from app.models import schemas
from app.models import orm
from app.dependencies import get_password_hash


def get_user(db: Session, user_id: int):
    return db.query(orm.User).filter(schemas.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_nft_art(db: Session, nft_id: int):
    return db.query(models.NFTArt).filter(models.NFTArt.id == nft_id).first()


def create_nft_art(db: Session, nft: schemas.NFTArtCreate, blockchain_id: str):
    db_nft = models.NFTArt(
        title=nft.title,
        description=nft.description,
        image_data=nft.image_data,
        blockchain_id=blockchain_id,
    )
    db.add(db_nft)
    db.commit()
    db.refresh(db_nft)
    return db_nft
