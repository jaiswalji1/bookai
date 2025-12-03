import pytest
from app.core.auth import create_access_token, decode_token

# Business Logic Tests
class TestBusinessLogic:
    # average rating calculation
    def test_average_rating_calculation(self):
        """Test average rating calculation"""
        ratings = [5, 4, 3, 4, 5]
        average = sum(ratings) / len(ratings)
        assert average == 4.2
    
    # rating between 1 and 5
    def test_rating_scale_validity(self):
        valid_ratings = [1, 2, 3, 4, 5]
        assert all(1 <= r <= 5 for r in valid_ratings)
    
    # timig of token expiration
    def test_token_expiration_logic(self):
        from datetime import datetime, timezone
        token = create_access_token("user", expires_minutes=30)
        payload = decode_token(token)
        
        # Check exp is in future
        current_time = datetime.now(timezone.utc).timestamp()
        assert payload["exp"] > current_time

if __name__ == "__main__":
    pytest.main([__file__, "-v"])