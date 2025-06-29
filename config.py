import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

class Config:
    def __init__(self):
        # Load environment variables each time Config is instantiated
        load_dotenv(override=True)
        
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
    
    MASKING_SEED = 12345  # Static seed for referential integrity
    
    @classmethod
    def reload(cls):
        """Reload environment variables"""
        load_dotenv(override=True)
        cls.DB_HOST = os.getenv("DB_HOST", "localhost")
        cls.DB_PORT = int(os.getenv("DB_PORT", 3306))
        cls.DB_USER = os.getenv("DB_USER", "root")
        cls.DB_PASSWORD = os.getenv("DB_PASSWORD", "")
        cls.SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")

