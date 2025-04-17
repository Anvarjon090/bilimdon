import os
from dotenv import load_dotenv
from piccolo.engine.postgres import PostgresEngine

# .env fayldan o'zgaruvchilarni yuklash
load_dotenv()

# .env dan o'qilgan ma'lumotlar
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# Piccolo uchun sinxron engine yaratish
engine = PostgresEngine(
    config={
        "database": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "host": DB_HOST,
        "port": DB_PORT,
    }
)

async def connect_to_db():
    await engine.begin()
    print("DB Connected!")