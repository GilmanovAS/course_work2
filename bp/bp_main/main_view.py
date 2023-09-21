from flask import Blueprint, render_template

from bp.bp_main.dao_main.dao_main_f import DaoPosts, DaoComments
from configs.config import PATH_JSON_POSTS, PATH_JSON_COMMENTS2

blueprint_main = Blueprint('blueprint_main', __name__, template_folder='templates_main')


@blueprint_main.route('/', methods=['GET'])
def main_page():
    posts = DaoPosts(PATH_JSON_POSTS)
    return render_template('index.html', posts=posts.get_posts_all())


@blueprint_main.route('/posts/<int:post_id>')
def post_page(post_id):
    post = DaoPosts(PATH_JSON_POSTS)
    comments = DaoComments(PATH_JSON_COMMENTS2)
    comments, comments_count = comments.get_comments_by_post_id(post_id)
    return render_template('post.html', post=post.get_post_by_pk(post_id),
                           comments=comments, comments_count=comments_count)
