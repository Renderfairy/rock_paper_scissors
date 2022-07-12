from http import HTTPStatus

from connexion import NoContent

from lib.models import Article, db


def get(user):
    articles = Article.query.filter(
        Article.author_user_id == user['user_id']
    ).all()

    return [
       {
           'article_id': article.article_id,
           'title': article.title,
           'content': article.content,
       }
       for article in articles
    ], HTTPStatus.OK


def post(user, body):
    db.session.add(Article(
        author_user_id=user['user_id'],
        title=body['title'],
        content=body['content'],
    ))
    db.session.commit()

    return NoContent, HTTPStatus.OK


def put(user, article_id, body):
    article = Article.query.filter(
        Article.article_id == article_id,
        Article.author_user_id == user['user_id'],
    ).first()

    if not article:
        return NoContent, HTTPStatus.NOT_FOUND

    article.title = body['title']
    article.content = body['content']
    db.session.commit()

    return NoContent, HTTPStatus.OK


def delete(user, article_id):
    Article.query.filter(
        Article.article_id == article_id,
        Article.author_user_id == user['user_id'],
    ).delete()

    db.session.commit()

    return NoContent, HTTPStatus.OK


