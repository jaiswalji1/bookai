import pytest
from app.core.security import hash_password, verify_password

# Security Tests
class TestSecurity:
    # hashing password
    def test_password_hashing(self):
        original_password = "test_password_123"
        hashed = hash_password(original_password)
        assert hashed != original_password
        assert len(hashed) > 0
    
    # verifying password
    def test_password_verification_success(self):
        password = "my_password_123"
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True
    
    # testing failed password verification
    def test_password_verification_failure(self):
        password = "my_password_123"
        hashed = hash_password(password)
        assert verify_password("wrong_password", hashed) is False
    
    # testing hashed response for two different passwords
    def test_different_passwords_different_hashes(self):
        hash1 = hash_password("password1")
        hash2 = hash_password("password2")
        assert hash1 != hash2
    
    # testing same password with different hashed values
    def test_same_password_multiple_hashes(self):
        """Test same password can verify against different hashes"""
        password = "test_password"
        hash1 = hash_password(password)
        hash2 = hash_password(password)
        # Both should verify the password
        assert verify_password(password, hash1) is True
        assert verify_password(password, hash2) is True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])