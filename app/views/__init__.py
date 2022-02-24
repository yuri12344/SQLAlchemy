from flask import Flask

def init_app(app: Flask) -> None:
    from .create_state import bp_create_state
    app.register_blueprint(bp_create_state)

    from .create_capital import bp_create_capital
    app.register_blueprint(bp_create_capital)