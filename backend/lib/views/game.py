from http import HTTPStatus
from connexion import NoContent
from lib.models import Win, Loss, Credit, db


def get_statistics(user):
    wins = Win.query.filter(Win.winner_id == user['user_id']).count()
    losses = Loss.query.filter(Loss.loser_id == user['user_id']).count()
    credits_available = Credit.query.filter(Credit.credit_owner_id == user['user_id']).first()

    return [
        {
            'Wins count': wins,
            'Losses count': losses,
            'Your credits': credits_available.credit_value
        }
    ], HTTPStatus.OK
