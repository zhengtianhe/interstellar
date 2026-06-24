from config import CONFIG

mysql = CONFIG['mysql']

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{mysql['user']}:"
    f"{mysql['password']}@"
    f"{mysql['host']}:"
    f"{mysql['port']}/"
    f"{mysql['database']}"
    f"?charset=utf8mb4"
)