from flask import Blueprint
from controllers.VideoController import index, filter_submit
videos_bp = Blueprint('video_bp', __name__)
videos_bp.route('/', methods=['GET'])(index)
videos_bp.route('/filter_submit', methods=['POST'])(filter_submit)