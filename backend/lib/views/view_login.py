from http import HTTPStatus

import bcrypt

from lib.auth import encode_token
from lib.models import User


def post(body):
    username: str = body['username']
    password: str = body['password']

    print(User.query.all())
    user = User.query.filter(
        User.username == username.strip(),
    ).first()

    if not user or not bcrypt.checkpw(password=password.encode('utf-8'), hashed_password=user.password_hash):
        return {}, HTTPStatus.UNAUTHORIZED

    token = encode_token(user.user_id)

    return {'authorization': 'Bearer ' + token}, HTTPStatus.OK


