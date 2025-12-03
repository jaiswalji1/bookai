from sqlalchemy import select, update, delete
from app.models.book import Book
from sqlalchemy.ext.asyncio import AsyncSession

class BookRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_book(self, payload):
        obj = Book(**payload)
        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)
        return obj
    
    async def fetch_all_book(self):
        query = select(Book)
        res = await self.db.execute(query)
        return res.scalars().all()
    
    async def fetch_book(self, book_id):
        query = select(Book).where(Book.id == book_id)
        res = await self.db.execute(query)
        return res.scalar_one_or_none()
    
    async def update_book(self, book_id, data= dict):
        query = update(Book).where(Book.id == book_id).values(**data).returning(Book)
        res = await self.db.execute(query)
        await self.db.commit()
        up_res = res.fetchone()
        if up_res:
            return up_res[0]
        else:
            return None
        
    async def delete_book(self, book_id):
        query = delete(Book).where(Book.id == book_id)
        await self.db.execute(query)
        await self.db.commit()
        return True

    

