from functools import wraps
from flask import request
from flask import jsonify
from utils.jwt_util import verify_token

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get(
            "Authorization"
        )

        if not auth:
            return jsonify({
                "msg":"token missing"
            }),401

        try:
            token = auth.split(" ")[1]

        except Exception:
            return jsonify({
                "msg":"token error"
            }),401

        payload = verify_token(token)
        if not payload:
            return jsonify({
                "msg":"token invalid"
            }), 401

        request.client = payload
        return  f(*args, **kwargs)

    return wrapper

def permission_required(scope):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth = request.headers.get(
                "Authorization"
            )
            token = auth.split(" ")[1]
            payload = verify_token(token)