from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class Quote(BaseModel):
    text: str
    character_id: Optional[UUID] = None
    created_at: datetime = datetime.now()


class UpdateQuote(BaseModel):
    text: Optional[str] = None
    character_id: Optional[UUID] = None
    created_at: Optional[datetime] = None