from typing import List
from app.repositories.book_repo import BookRepo
from config import settings

class RecommendationService:
    def __init__(self, db):
        self.db = db

    async def recommend_by_gener(self, gener: str, limit : int = settings.LIMIT):
        repo = BookRepo(self.db)
        book = await repo.fetch_all_book()
        recommended_book = []
        for row in book:
            if row.gener and gener.lower() in (row.gener or "").lower():
                recommended_book.append(row)
        return recommended_book[:limit]
