from datetime import timedelta

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app.schemas.user_schema import UserSchema
from flask import Blueprint, make_response, jsonify, request
from app import app,db
from app.services.user_service import UserService
from app.services.auth_service import AuthService
user_schema = UserSchema()

user_blueprint = Blueprint('user', __name__)


@app.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    try:
        current_user = get_jwt_identity()
        userLogged = UserService.get_user_by_id(current_user)
        print("User", user_schema.dump(userLogged))
        users = UserService.get_all_users()
        result = user_schema.dump(users, many=True)
        return make_response(jsonify({"users": result}))
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route('/auth/register', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        print(data)

        # errors = user_schema.validate(data, session=db.session)
        # if errors:
        #     return make_response(jsonify(errors), 400)

        user = UserService.create_user(data)
        result = user_schema.dump(user)
        return make_response(jsonify({"user": result}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@app.route('/auth/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()

        if data['password'] is None or data['email'] is None:
            return make_response(jsonify({'error': 'Email and Password both are required'}),400)

        user = UserService.get_user_by_email(data['email'])

        if user is None:
            return make_response(jsonify({"error": "User does not exist"}), 404)

        password_match = user.check_password(data['password'])
        if not password_match:
            return make_response(jsonify({"error": "Invalid password"}), 400)

        access_token = AuthService.gen_access_token(user.id)
        return make_response(jsonify({"access_token": access_token}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)