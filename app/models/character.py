from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date

class Character(BaseModel):
    name: str
    surname: Optional[str] = None
    nickname: Optional[str] = None
    bio: Optional[str] = None
    date_of_birth: date
    date_of_death: Optional[date] = None
    origin: Optional[str] = None
    image_url: Optional[HttpUrl] = None

class CharacterUpdate(BaseModel): 
   name: Optional[str]
   surname: Optional[str]
   nickname: Optional[str] 
   bio: Optional[str] 
   date_of_birth: Optional[date]
   date_of_death: Optional[date] = None
   origin: Optional[str] 
   image_url: Optional[HttpUrl]