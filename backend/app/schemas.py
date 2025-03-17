from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class NoteBase(BaseModel):
    text: str = Field(..., min_length=1, max_length=1500)
    tag: str = Field(..., min_length=1, max_length=100)
    create_at: datetime = Field(default_factory=datetime.utcnow)


class NoteCreate(NoteBase):
    pass


class NoteRead(NoteBase):
    id: int

    model_config = {'from_attributes': True}


class NoteUpdate(BaseModel):
    text: Optional[str] = Field(None, min_length=1, max_length=1500)
    tag: Optional[str] = Field(None, min_length=1, max_length=100)


