from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class NFTArt(Base):
    __tablename__ = "nftart"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    image_data = Column(LargeBinary)
    blockchain_id = Column(String, unique=True)
    access_count = Column(Integer, default=0)
