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

    # JWT session tokens. The dev fallback secret is fine for local/test use
    # (matches the rest of this file's "fallback for dev/test" pattern) but
    # MUST be overridden via a real env var in any deployed environment.
    JWT_SECRET_KEY: str = "dev-only-insecure-secret-change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    model_config = SettingsConfigDict(env_file=env_file)

settings = Settings()
