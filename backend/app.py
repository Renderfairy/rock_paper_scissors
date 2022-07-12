from lib.config import CONFIG


def build_app():
    import connexion as connexion
    from lib.models import db

    debug_mode = (CONFIG.ENVIRONMENT != 'production')
    app = connexion.App(__name__, specification_dir='lib/', debug=debug_mode)

    app.add_api('api_spec.yaml', base_path='/api', validate_responses=debug_mode, options={"swagger_ui": debug_mode})

    flask_app = app.app

    # activate config
    flask_app.config.from_object(CONFIG)

    db.init_app(flask_app)

    if debug_mode:
        @flask_app.before_request
        def log_request_info():
            import logging
            from flask import request
            logging.info(f'Body: {request.data}')

    return flask_app


app = build_app()

#if __name__ == '__main__':
#    app.run(port=8080)
