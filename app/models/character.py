from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date

class Character(BaseModel):
    name: str
    nickname: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: date
    date_of_death: Optional[date] = None
    origin: Optional[str] = None
    image_url: HttpUrl