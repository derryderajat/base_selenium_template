import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    BROWSER = "chrome"
    TIMEOUT = 10 