import os

class Settings:
    PROJECT_NAME: str = 'Attendance Tracker'
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'sqlite:///./data.db')

settings = Settings()
