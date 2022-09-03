from flask import Blueprint
from controllers.VideoController import index
videos_bp = Blueprint('video_bp', __name__)
videos_bp.route('/', methods=['GET'])(index)
videos_bp.route('/videos', methods=['GET'])(index)

# videos_bp.route('/create', methods=['POST'])(store)
# videos_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
# videos_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)