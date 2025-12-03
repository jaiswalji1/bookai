from fastapi import APIRouter, Depends
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.recommendation_service import RecommendationService
from app.core.auth import get_current_user
from app.schemas.recommendation import Recommendation

router = APIRouter(tags=["recommendation"])

@router.get("/recommendation")
async def recommendations(payload: Recommendation, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    ser = RecommendationService(db)
    return await ser.recommend_by_gener(payload.gener)