from http import HTTPStatus
from connexion import NoContent
from lib.models import Win, Loss, Credit, db
from lib.game.game_logic import rock_paper_scissors


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


def play_game(user, choice):

    game_play = rock_paper_scissors(choice)

    if game_play['message'] == 'You won!':
        user_credits = Credit.query.filter(Credit.credit_owner_id == user['user_id']).first()
        user_credits.credit_value += 4
        db.session.add(Win(winner_id=user['user_id']))
        db.session.commit()
        return game_play,  HTTPStatus.OK
    elif game_play['message'] == 'You lost.':
        db.session.add(Loss(loser_id=user['user_id']))
        db.session.commit()
        return game_play, HTTPStatus.OK
    else:
        return game_play, HTTPStatus.OK

