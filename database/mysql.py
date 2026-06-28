from config import CONFIG
from sqlalchemy import create_engine, text

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

# 🚀 关键优化：连接池 + 性能参数
engine = create_engine(
    DATABASE_URL,

    pool_size=10,  # 常驻连接
    max_overflow=20,  # 峰值连接
    pool_recycle=3600,  # 1小时回收
    pool_pre_ping=True,  # 自动检测断线

    future=True,  # SQLAlchemy 2.0 风格
    echo=True  # 生产关闭日志
)


class MYSQLDB:
    def __init__(self):
        self.url = DATABASE_URL

    # ---------------- 查询 ----------------
    def select_one(self, sql, params = None):
        with engine.connect() as conn:
            result = conn.execute(text(sql), params or {})
            row = result.mappings().first()

            return dict(row) if row else None

