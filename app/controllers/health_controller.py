from flask import Blueprint, jsonify
import logging

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

health_controller = Blueprint('health_controller', __name__)

@health_controller.route('/health', methods=['GET'])
def health_check():
    logger.info("Liveness check endpoint called.")
    return jsonify({"status": "OK"}), 200

@health_controller.route('/liveness', methods=['GET'])
def liveness_check():
    logger.info("Liveness check endpoint called.")
    return jsonify({"status": "OK"}), 200
