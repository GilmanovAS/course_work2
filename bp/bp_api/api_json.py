from flask import Blueprint, jsonify

from bp.bp_api.dao_api.dao_api_f import DaoApi
from configs.config import PATH_JSON_POSTS

blueprint_api = Blueprint('blueprint_api', __name__)


@blueprint_api.route('/api/posts')
def api_page():
    return jsonify(DaoApi(PATH_JSON_POSTS).get_posts_all())


@blueprint_api.route('/api/posts/<int:pk>')
def api_page_by_id(pk):
    return jsonify(DaoApi(PATH_JSON_POSTS).get_post_by_pk(pk))
