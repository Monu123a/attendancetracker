import os

class Config:
    DB_URL = os.getenv('DATABASE_URL', 'sqlite:///./data.db')
