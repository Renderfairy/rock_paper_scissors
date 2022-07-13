import os

from app import app
from lib.config import CONFIG
from lib.models import db, User


def setup_db():
    if 'production' in os.getenv('APP_SETTINGS', '').lower() or CONFIG.ENVIRONMENT == 'production':
        app.logger.error('restore_staging_dataset cannot be used in production env!!!')
        exit()

    with app.app_context():
        db.drop_all()
        db.create_all()

        user = User(username='test', password='test')
        db.session.add(user)
        db.session.flush()  # required to create user_id

        db.session.commit()


if __name__ == '__main__':
    setup_db()
