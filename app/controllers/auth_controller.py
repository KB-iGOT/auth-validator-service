
from flask import Blueprint, request, jsonify
from ..services.auth_service import AuthService
from constants import X_AUTHENTICATED_USER_TOKEN
import logging

# Blueprint instance for this controller
auth_controller = Blueprint('auth_controller', __name__)

auth_service = AuthService()

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

@auth_controller.route('/auth/validate', methods=['GET'])
def validate_auth():
    """
    Endpoint for authentication validation.
    Expects 'x-authenticated-user-token' in request headers.
    """
    token = request.headers.get(X_AUTHENTICATED_USER_TOKEN)
    logger.debug("The token is " + token)
    if not token:
        return jsonify({"error": "Missing authentication token"}), 401

    is_valid = auth_service.is_valid_token(token)
    logger.info("Is Token valid: " + str(is_valid))
    if is_valid:
        return jsonify({"message": "Token is valid"}), 200
    else:
        return jsonify({"error": "Invalid token"}), 401
