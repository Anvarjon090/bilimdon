from piccolo.engine.postgres import PostgresEngine
from piccolo.conf.apps import AppRegistry


DATABASE = {
    "dbname": "dbname",  
    "user": "Anvar",
    "password": "anvar090",
    "host": "localhost",  
    "port": 5432,  
}

# Piccolo ilovalarini ro'yxatga olish
APP_REGISTRY = AppRegistry(
    apps=[
        # Bu yerda Piccolo ilovalaringizni ro'yxatga olishingiz mumkin
    ]
)

# Postgres ma'lumotlar bazasi ulanishini sozlash
DB = PostgresEngine(
    dbname=DATABASE["dbname"],  # "database" o'rniga "dbname" ishlatiladi
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE.get("host", "localhost"),  # Agar host ko'rsatilmasa, localhost bo'ladi
    port=DATABASE.get("port", 5432)  # Agar port ko'rsatilmasa, 5432 bo'ladi
)