
from flask import Flask
import logging
import gc
from app.authentication.KeyManager import KeyManager
from constants import ACCESS_TOKEN_PUBLICKEY_BASEPATH


# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)

    base_path = ACCESS_TOKEN_PUBLICKEY_BASEPATH
    if not base_path:
        logger.error("ACCESS_TOKEN_PUBLICKEY_BASEPATH is not set.")
        raise ValueError("ACCESS_TOKEN_PUBLICKEY_BASEPATH is not set.")
    KeyManager.init(base_path)
    logger.info("KeyManager initialized successfully.")

    try:
        from app.controllers.auth_controller import auth_controller
        app.register_blueprint(auth_controller)
        from app.controllers.health_controller import health_controller
        app.register_blueprint(health_controller)
    except Exception as e:
        app.logger.error(f"Blueprint registration failed: {e}")
        raise

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        # Force garbage collection after request
        gc.collect()

    return app
