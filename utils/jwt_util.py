import jwt
from datetime import datetime, timedelta, UTC
SECRET_KEY = "7d7d7bff4d78a9b0f1dbdf8b2e1e8c7d2b7f8f4f9c4f3b8a7c6d5e4f3a2b1c0d"
ALGORITHM = "HS256"
def create_access_token(user):
    payload = {
        "user_id":user["id"],
        "username":user["username"],
        "type":"access",
        "exp":datetime.now(UTC) + timedelta(hours=2),
        "iat":datetime.now(UTC)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
def create_refresh_token(user):
    payload = {
        "user_id":user["id"],
        "username":user["username"],
        "type":"refresh",
        "exp":datetime.now(UTC) + timedelta(days=30)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )
def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# def generate_token(client_id, scope):
#     payload = {
#         "client_id":client_id,
#         "scope":scope,
#         "exp":datetime.now(UTC) + timedelta(hours=2),
#         "iat":datetime.now(UTC)
#     }
#
#     return jwt.encode(
#         payload,
#         SECRET_KEY,
#         algorithm="HS256"
#     )
#
# def verify_token(token):
#     try:
#         payload = jwt.decode(
#             token,
#             SECRET_KEY,
#             algorithms=["HS256"]
#         )
#         return payload
#     except jwt.ExpiredSignatureError:
#         return None
#     except jwt.InvalidTokenError:
#         return None