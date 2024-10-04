from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI","mongodb://localhost:27017/corider")
    SECRET_KEY = os.getenv(key="SECRET_KEY")
