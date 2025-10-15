from pydantic_settings import BaseSettings, SettingsConfigDict
import os

env_file = ".env" if os.getenv("ENV", "dev") == "dev" else ".env.live"

class Settings(BaseSettings):
    ENV: str = "dev"

    ALLOWED_ORIGINS: str = "*"  # ✅ fallback for dev/test
    DATABASE_URL: str = "sqlite:///./test.db"  # ✅ fallback for test runs

    CLOUDINARY_CLOUD_NAME: str = "dummy"
    CLOUDINARY_API_KEY: str = "dummy"
    CLOUDINARY_API_SECRET: str = "dummy"

    SMTP_HOST: str = "dummy"
    SMTP_PORT: str = "dummy"
    SMTP_USER: str = "dummy"
    SMTP_PASS: str = "dummy"

    model_config = SettingsConfigDict(env_file=env_file)

settings = Settings()
