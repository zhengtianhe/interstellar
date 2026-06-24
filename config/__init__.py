import json
import os
from dotenv import load_dotenv

load_dotenv()

CONFIG_FILE = os.getenv(
    "CONFIG_FILE",
    "config/dev.json"
)
with open(CONFIG_FILE, "r", encoding="utf8") as f:
    CONFIG = json.load(f)