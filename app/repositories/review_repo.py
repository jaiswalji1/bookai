from sqlalchemy import select, update, delete
from app.models.review import Review
from sqlalchemy.ext.asyncio import AsyncSession

class ReviewRepo:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_review(self, payload):
        obj = Review(**payload)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
    
    async def fetch_book_review(self, book_id):
        query = select(Review).where(Review.book_id == book_id)
        res = await self.db.execute(query)
        return res.scalars().all()
    
    async def fetch_summary_aggr_rating(self, book_id):
        query = select(Review.rating).where(Review.book_id == book_id)
        res = await self.db.execute(query)
        ratings = [r for (r,) in res.all()]
        if not ratings:
            return None
        else:
            return sum(ratings)/len(ratings)