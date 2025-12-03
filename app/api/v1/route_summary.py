from fastapi import APIRouter, Depends, HTTPException
from app.db.session import get_db
from app.services.summary_service import SummaryService
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.book_repo import BookRepo
from app.repositories.review_repo import ReviewRepo
from app.core.auth import get_current_user

router = APIRouter(tags=["summary"])

@router.post("/generate-summary")
async def generate_summary(payload: dict , user=Depends(get_current_user)):
    text = payload.get("text",'')
    ai = SummaryService()
    summary = await ai.generate_summary(text)
    return {"summary":summary}

@router.get("/books/{book_id}/summary")
async def book_summary(book_id: int, db:AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    book_repo =BookRepo(db)
    book = await book_repo.fetch_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    review_repo =ReviewRepo(db)
    avg = await review_repo.fetch_summary_aggr_rating(book_id)
    return {"summary": book.summary or "", "avg_rating": avg}