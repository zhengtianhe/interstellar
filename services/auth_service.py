from models.user import User
from utils.password_util import PasswordUtil
from utils.jwt_util import create_access_token, create_refresh_token,verify_token
class AuthService:
    @staticmethod
    def login_by_password(username, password):
        user = User.query_by_username(username)
        if not user:
            return {
                "code":404,
                "msg":"用户不存在"
            }
        hashed_password = user.get("password")
        if not PasswordUtil.verify_password(password,hashed_password):
            return {
                "code":401,
                "msg":"密码错误"
            }
        access_token = create_access_token(user)
        refresh_token = create_refresh_token(user)
        return {
            "code":0,
            "msg":"登陆成功",
            "data":{
                "access_token":access_token,
                "refresh_token":refresh_token
            }
        }
    @staticmethod
    def refresh_access_token(refresh_token):
        payload = verify_token(refresh_token)
        if payload is None:
            return {
                "code": 401,
                "msg":"Refresh Token无效"
            }
        token_type = payload.get("type", None)
        if token_type != "refresh":
            return {
                "code":401,
                "msg":"Token类型错误"
            }
        user_id = payload.get("user_id")
        if not user_id:
            return {
                "code":401,
                "msg":"用户不存在"
            }
        user = User.query_by_userid(user_id)
        if not user:
            return {
                "code": 401,
                "msg": "用户不存在"
            }
        access_token = create_access_token(user)
        return {
            "code":0,
            "msg":"刷新成功",
            "data":{
                "access_token":access_token
            }
        }