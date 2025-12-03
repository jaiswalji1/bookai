import pytest
from app.schemas.book import BookCreate
from app.schemas.review import ReviewCreate

# Data Transformation Tests
class TestDataTransformation:
    # converting book schemas to dicts
    def test_book_schema_to_dict(self):
        book = BookCreate(title="Test", author="Author")
        book_dict = book.model_dump()
        assert book_dict["title"] == "Test"
        assert book_dict["author"] == "Author"
    
    # converting review schemas to dicts
    def test_review_schema_to_dict(self):
        review = ReviewCreate(user_id="user1", review_text="Good", rating=4)
        review_dict = review.model_dump()
        assert review_dict["user_id"] == "user1"
        assert review_dict["review_text"] == "Good"
        assert review_dict["rating"] == 4

if __name__ == "__main__":
    pytest.main([__file__, "-v"])