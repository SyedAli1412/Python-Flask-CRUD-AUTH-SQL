from datetime import timedelta

from flask_jwt_extended import create_access_token


class AuthService:

    @staticmethod
    def gen_access_token(id):
        return create_access_token(identity=id, expires_delta=timedelta(minutes=10))
