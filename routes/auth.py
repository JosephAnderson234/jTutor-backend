from flask import Blueprint, request
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

# MVP: usuario mock
USERS = {
    "test@test.com": "123456"
}

@auth_bp.post("/login")
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if USERS.get(email) != password:
        return {"msg": "Credenciales inválidas"}, 401

    token = create_access_token(identity=email)
    return {"access_token": token}
