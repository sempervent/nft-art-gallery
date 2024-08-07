from pydantic import BaseModel


class Art(BaseModel):
    title: str
    description: str
    image_url: str
    price: float
