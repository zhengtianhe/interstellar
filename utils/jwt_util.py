import jwt
from datetime import datetime, timezone
SECRET_KEY = "crm-api-secret"

def create_access_token(client_id, scope):
    payload = {
        "client_id":client_id,
        "scope":scope,
        "exp":datetime.utcnow()
    }

