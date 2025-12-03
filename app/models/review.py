import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.sql import func

class Review(Base):
    __tablename__ = "reviews"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    book_id = sa.Column(sa.Integer, sa.ForeignKey("books.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = sa.Column(sa.String(64), nullable=False)
    review_text = sa.Column(sa.Text, nullable=False)
    rating = sa.Column(sa.Integer, nullable=False)
    created_at = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
    book = relationship("Book", back_populates="reviews")