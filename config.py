from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:Admin123$@localhost:5432/bookai"
    SECRET_KEY: str = "LtTTTeAQaXadSB4PD_Ec1b9rEnHAWqjmXteN58BTh2k"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24
    OLLAMA_MODEL: str = "qwen3:4b"
    Title: str = "BookAI"
    ALGORITHM: str = "HS256"
    LIMIT: int = 10

    class Config:
        env_file = ".env"

settings = Settings()