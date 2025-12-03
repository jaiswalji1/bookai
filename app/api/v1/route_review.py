from fastapi import APIRouter, HTTPException, Depends
from app.schemas.review import *
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.book_repo import BookRepo
from app.repositories.review_repo import ReviewRepo
from app.core.auth import get_current_user

router = APIRouter(prefix="/books/{book_id}/reviews", tags=["reviews"])

@router.post("/", response_model=ReviewOut)
async def add_review(book_id: int, payload: ReviewCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    book_res = BookRepo(db)
    ## if book exists
    book = await book_res.fetch_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    repo = ReviewRepo(db)
    data = payload.model_dump()
    data["book_id"] = book_id
    review = await repo.create_review(data)
    return review

@router.get("/", response_model=list[ReviewOut])
async def list_review(book_id: int , db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    repo = ReviewRepo(db)
    return await repo.fetch_book_review(book_id)
