import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.sql import func

class Book(Base):
    __tablename__ = "books"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title =sa.Column(sa.String(255), nullable=False, index=True)
    author = sa.Column(sa.String(255), nullable=True)
    gener = sa.Column(sa.String(100), nullable=True)
    year_published = sa.Column(sa.Integer, nullable=True)
    summary = sa.Column(sa.Text, nullable=True)
    created_at = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
    updated_at = sa.Column(sa.DateTime(timezone=True), onupdate=func.now())
    reviews = relationship("Review", back_populates="book", cascade="all, delete-orphan")

