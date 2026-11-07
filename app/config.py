from pydantic_settings import BseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/fastapi_db"

    class Config:
        env_file = ".env"

settings = Settings()