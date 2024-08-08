from pydantic import BaseModel


class Art(BaseModel):
    title: str
    description: str
    image_url: str
    price: float


class UserCreate(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class NFTArtBase(BaseModel):
    title: str
    description: str


class NFTArtCreate(NFTArtBase):
    image_data: bytes


class NFTArt(NFTArtBase):
    id: int
    blockchain_id: str
    access_count: int

    class Config:
        orm_mode = True
