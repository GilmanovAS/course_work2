import logging

from flask import Blueprint, render_template, request

from bp.bp_main.dao_main.dao_main_f import DaoPosts, DaoComments
from configs.config import PATH_JSON_POSTS, PATH_JSON_COMMENTS

blueprint_main = Blueprint('blueprint_main', __name__, template_folder='templates_main')


def add_a_tag(st):
    return f'<a href="/tag/{st[1:]}">{st}</a>'


def change_tag_content(post):
    content = post['content'].split()
    for item in enumerate(content):
        if '#' == item[1][0]:
            content[item[0]] = add_a_tag(content[item[0]])
    post['content'] = ' '.join(content)
    return post


@blueprint_main.route('/', methods=['GET'])
def main_page():
    posts = DaoPosts(PATH_JSON_POSTS)
    logging.info("index.html")
    return render_template('index.html', posts=posts.get_posts_all_short())


@blueprint_main.route('/posts/<int:post_id>')
def post_page(post_id):
    logging.info(f"/posts/{post_id}")
    post = DaoPosts(PATH_JSON_POSTS)
    comments_o = DaoComments(PATH_JSON_COMMENTS)
    comments_l, comments_count = comments_o.get_comments_by_post_id(post_id)
    post = post.get_post_by_pk(post_id)
    post = change_tag_content(post)
    return render_template('post.html', post=post,
                           comments=comments_l, comments_count=comments_count)


@blueprint_main.route('/user-feed/<user_name>')
def posts_by_user_page(user_name):
    logging.info(f"/user-feed/{user_name}")
    posts_o = DaoPosts(PATH_JSON_POSTS)
    posts_l = posts_o.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts_l)


@blueprint_main.route('/search/<search_str>')
def search_page(search_str):
    logging.info(f"/search/{search_str}")
    posts_o = DaoPosts(PATH_JSON_POSTS)
    posts_l, count = posts_o.search_for_posts(search_str)
    return render_template('search.html', posts=posts_l, count=count)


@blueprint_main.route('/search/', methods=['GET'])
def search_page_request():
    posts_o = DaoPosts(PATH_JSON_POSTS)
    search_str = request.values.get('search')
    logging.info(f"/search/?search={search_str}")
    posts_l, count = posts_o.search_for_posts(search_str)
    return render_template('search.html', posts=posts_l, count=count)

@blueprint_main.route('/tag/<tagname>')
def tag_page(tagname):
    return render_template('tag.html')
