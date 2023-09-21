from flask import Blueprint, render_template

from bp.bp_main.dao_main.dao_main_f import DaoMain
from configs.config import PATH_JSON_POSTS

blueprint_main = Blueprint('blueprint_main', __name__, template_folder='templates_main')


@blueprint_main.route('/', methods=['GET'])
def main_page():
    posts = DaoMain(PATH_JSON_POSTS)
    return render_template('index.html', posts=posts.get_posts_all())
