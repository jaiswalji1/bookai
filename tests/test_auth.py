import pytest
from app.core.auth import create_access_token, decode_token

#Authentication Test
class TestAuthentication:
    #generating the token for user
    def test_create_user_token(self):
        token = create_access_token("testuser", role="user")
        assert token is not None
        assert len(token) > 0
    
    #generating the token for admin
    def test_create_admin_token(self):
        token = create_access_token("admin", role="admin")
        payload = decode_token(token)
        assert payload["role"] == "admin"
    
    #decoding valid token
    def test_decode_valid_token(self):
        token = create_access_token("testuser", role="user")
        payload = decode_token(token)
        assert payload["sub"] == "testuser"
        assert payload["role"] == "user"
        assert "exp" in payload
    
    #decoding invalid token and raising exception
    def test_decode_invalid_token(self):
        with pytest.raises(Exception):
            decode_token("invalid.token.here")
    
    #token expiration test
    def test_token_has_expiration(self):
        token = create_access_token("user", expires_minutes=30)
        payload = decode_token(token)
        assert "exp" in payload
    
    #token custom expiration time test
    def test_custom_expiration_time(self):
        token = create_access_token("user", expires_minutes=60)
        payload = decode_token(token)
        assert payload["sub"] == "user"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
