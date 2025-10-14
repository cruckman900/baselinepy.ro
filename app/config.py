import os
from pydantic_settings import BaseSettings, SettingsConfigDict

env_file = ".env.test" if os.getenv("ENV", "dev") == "dev" else ".env"

class Settings(BaseSettings):
    ENV: str = "dev"

    ALLOWED_ORIGINS: str
    # RENDER_API_KEY: str
    DATABASE_URL: str
    # DEBUG_MODE: bool = False

    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()