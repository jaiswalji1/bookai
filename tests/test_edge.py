import pytest
from app.schemas.book import BookCreate
from app.schemas.review import ReviewCreate

# Edge Case Tests
class TestEdgeCases:
    # book with empty title
    def test_empty_book_title(self):
        book = BookCreate(title="")
        assert book.title == ""
    
    # book with long title above 255 characters
    def test_very_long_book_title(self):
        long_title = "A" * 500
        book = BookCreate(title=long_title)
        assert len(book.title) == 500
    
    # testing special characters in review text
    def test_special_characters_in_review(self):
        review = ReviewCreate(
            user_id="user@123",
            review_text="Great! 📚 Amazing!!",
            rating=5
        )
        assert "📚" in review.review_text
    
    # testing whitespace/blankspace in book fields
    def test_whitespace_in_fields(self):
        """Test fields with whitespace"""
        book = BookCreate(title="  Book Title  ", author="  Author Name  ")
        assert book.title == "  Book Title  "
        assert book.author == "  Author Name  "

if __name__ == "__main__":
    pytest.main([__file__, "-v"])