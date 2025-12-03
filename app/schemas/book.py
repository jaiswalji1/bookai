from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: Optional[str] = None
    gener: Optional[str] = None
    year_published: Optional[int] = None

class BookCreate(BookBase):
    summary: Optional[str] = None

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    gener: Optional[str]
    year_published: Optional[int]
    summary: Optional[str]

class BookOut(BookBase):
    id: int
    summary: Optional[str] = None
    created_at: Optional[datetime]
    class Config:
        from_attributes = True

        