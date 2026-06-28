from flask import Blueprint
from flask import jsonify
from flask import request
from services.auth_service import AuthService

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)

@auth_bp.route(
    "/login/password",
    methods=["POST"]
)

def login():
    if not request.is_json:
        return jsonify({
            "code":400,
            "msg":"Content-Type 必须是 application/json"
        }), 400
    data = request.get_json()
    if data is None:
        return jsonify({
            "code":400,
            "msg":"请求体不是合法 JSON"
        }), 400

    username = data.get("username", "").strip()
    password = data.get("password")
    if not username:
        return jsonify({
            "code":400,
            "msg":"用户名不能为空"
        }), 400
    if not password:
        return jsonify({
            "code":400,
            "msg":"密码不能为空"
        }), 400

    result = AuthService.login_by_password(username, password)
    return jsonify(result)

@auth_bp.route(
    "/refresh",
    methods=["POST"]
)

def refresh():
    if not request.is_json:
        return jsonify({
            "code":400,
            "msg":"Content-Type 必须是 application/json"
        }), 400
    data = request.get_json()
    if not data:
        return jsonify({
            "code":400,
            "msg":"请求数据不能为空"
        }),400
    refresh_token = data.get("refresh_token")
    if not refresh_token:
        return jsonify({
            "code":400,
            "msg":"refresh_token不能为空"
        }),400
    result = AuthService.refresh_access_token(
        refresh_token
    )
    return jsonify(result)

