import uvicorn
from fastapi import FastAPI
from config import settings
from app.api.v1.route_auth import router as route_auth
from app.api.v1.route_book import router as route_book
from app.api.v1.route_recommendations import router as route_recommendations
from app.api.v1.route_review import router as route_review
from app.api.v1.route_summary import router as route_summary

app = FastAPI(title=settings.Title)

app.include_router(route_auth)
app.include_router(route_book)
app.include_router(route_recommendations)
app.include_router(route_review)
app.include_router(route_summary)

@app.get("/")
async def root():
    return {"ok": True}
