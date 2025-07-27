from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date
from uuid import UUID

class Media(BaseModel):
    title: str
    file_url: HttpUrl
    character_id: Optional[UUID] = None
    created_at: Optional[date] = None

class UpdateMedia(BaseModel):
    title: Optional[str] = None
    file_url: Optional[HttpUrl] = None
    character_id: Optional[UUID] = None
    created_at: Optional[date] = None