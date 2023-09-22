from flask import Blueprint, render_template

from bp.bp_main.dao_main.dao_main_f import DaoPosts, DaoComments
from configs.config import PATH_JSON_POSTS, PATH_JSON_COMMENTS

blueprint_main = Blueprint('blueprint_main', __name__, template_folder='templates_main')


@blueprint_main.route('/', methods=['GET'])
def main_page():
    posts = DaoPosts(PATH_JSON_POSTS)
    return render_template('index.html', posts=posts.get_posts_all_short())


@blueprint_main.route('/posts/<int:post_id>')
def post_page(post_id):
    post = DaoPosts(PATH_JSON_POSTS)
    comments_o = DaoComments(PATH_JSON_COMMENTS)
    comments_l, comments_count = comments_o.get_comments_by_post_id(post_id)
    return render_template('post.html', post=post.get_post_by_pk(post_id),
                           comments=comments_l, comments_count=comments_count)


@blueprint_main.route('/user-feed/<user_name>')
def posts_by_user_page(user_name):
    posts_o = DaoPosts(PATH_JSON_POSTS)
    posts_l = posts_o.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts_l)


@blueprint_main.route('/search/<search_str>')
def search_page(search_str):
    posts_o = DaoPosts(PATH_JSON_POSTS)
    posts_l, count = posts_o.search_for_posts(search_str)
    return render_template('search.html', posts=posts_l, count=count)
