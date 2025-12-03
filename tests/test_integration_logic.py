import pytest
from app.core.auth import create_access_token, decode_token
from app.core.security import hash_password, verify_password
from app.schemas.book import BookCreate
from app.schemas.review import ReviewCreate

# Integration Logic Tests
class TestIntegrationLogic:
    # testing user authentication 
    def test_auth_flow_complete(self):
        # Step 1: Create token
        token = create_access_token("john", role="user")
        assert token
        
        # Step 2: Decode token
        payload = decode_token(token)
        assert payload["sub"] == "john"
        assert payload["role"] == "user"
    
    # testing flow for password validation
    def test_password_auth_flow(self):
        # Step 1: Hash password on signup
        raw_password = "MyPassword123!"
        hashed = hash_password(raw_password)
        
        # Step 2: Verify password on login
        is_valid = verify_password(raw_password, hashed)
        assert is_valid
    
    # testing book and review creation workflow
    def test_book_review_workflow(self):
        # Create book
        book = BookCreate(
            title="Great Book",
            author="John",
            gener="Fiction"
        )
        assert book.title == "Great Book"
        
        # Create review for book
        review = ReviewCreate(
            user_id="user1",
            review_text="Amazing!",
            rating=5
        )
        assert review.rating == 5

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
