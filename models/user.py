from database.mysql import MYSQLDB

class User:
    def __init__(self):
        pass

    @staticmethod
    def query_by_username(username):
        sql = """
        SELECT * FROM users WHERE username = :username
        """
        user = MYSQLDB().select_one(sql, {
            "username":username
        })
        return user
    @staticmethod
    def query_by_userid(user_id):
        sql = """
        SELECT * FROM users WHERE id = :id
        """
        user = MYSQLDB().select_one(sql, {
            "id":user_id
        })
        return user