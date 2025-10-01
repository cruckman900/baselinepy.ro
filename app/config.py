from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # RENDER_API_KEY: str
    # DATABASE_URL: str
    # DEBUG_MODE: bool = False

    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()