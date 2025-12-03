from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class ReviewCreate(BaseModel):
    user_id: str
    review_text: str
    rating: int = Field(..., ge=1, le=5)

class ReviewOut(ReviewCreate):
    id: int
    created_at: Optional[datetime]
    class Config:
        from_attributes = True