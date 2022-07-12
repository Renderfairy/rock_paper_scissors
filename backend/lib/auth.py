"""
More on JWT tokens: https://jwt.io/
"""

import logging
from datetime import datetime, timedelta

import jwt

from lib.config import CONFIG

ALGORITHM = 'HS256'


def decode_token(token):
    try:
        print(token)
        return jwt.decode(
            token,
            CONFIG.SECRET_KEY,
            options={"require": ["exp", "iss", "sub", "iat"]},
            algorithms=[ALGORITHM])
    except jwt.DecodeError:
        logging.debug(f'Token decoding error')
        return None
    except jwt.ExpiredSignatureError:
        logging.debug(f'Token signature expired')
        return None
    except jwt.InvalidIssuerError:
        logging.debug(f'Invalid token issuer')
        return None
    except jwt.InvalidTokenError:
        logging.debug(f'Unknown error')
        return None


def encode_token(user_id):
    timestamp_now = int(datetime.utcnow().timestamp())
    token = jwt.encode({
        'iss': 'change_me',
        'iat': timestamp_now,
        "exp": timestamp_now + timedelta(hours=24).total_seconds(),
        "sub": dict(
            user_id=user_id,
        )
    }, CONFIG.SECRET_KEY, algorithm=ALGORITHM)

    return token