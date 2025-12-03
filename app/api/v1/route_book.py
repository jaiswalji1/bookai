from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from app.db.session import get_db
from app.schemas.book import *
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.book_repo import BookRepo
from app.core.auth import get_current_user
from app.services.summary_service import SummaryService

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=BookOut)
async def create_book(payload: BookCreate, background_task: BackgroundTasks , db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    repo = BookRepo(db)
    data = payload.model_dump()
    book = await repo.create_book(data)
    if not book.summary:
        ai_summary = SummaryService()
        background_task.add_task(generate_and_save_summary, ai_summary, db, book.id)
    return book

@router.get("/", response_model=list[BookOut])
async def list_books(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    res = BookRepo(db)
    return await res.fetch_all_book()

@router.get("/{book_id}", response_model=BookOut)
async def fetch_book(book_id: int, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    res = BookRepo(db)
    book = await res.fetch_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")
    return book

@router.put("/{book_id}", response_model=BookOut)
async def update_book(book_id: int, payload: BookUpdate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    res = BookRepo(db)
    data = {k:v for k,v in payload.model_dump().items() if v is not None}
    update = await res.update_book(book_id, data)
    if not update:
        raise HTTPException(status_code=404, detail="Not Found")
    return update

@router.delete("/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db), user= Depends(get_current_user)):
    repo = BookRepo(db)
    await repo.delete_book(book_id)
    return {"message":"Book has been deleted", "ok": True}

async def generate_and_save_summary(ai: SummaryService, db: AsyncSession, book_id: int):
    repo = BookRepo(db)
    book = await repo.fetch_book(book_id)
    if not book:
        return {"ok": False}
    summary = await ai.generate_summary((book.title or "") + "\n\n" + (book.summary or ""))
    await repo.update_book(book_id, {"summary": summary})


