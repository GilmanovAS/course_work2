import logging

from flask import Blueprint, render_template, request, redirect

from bp.bp_main.dao_main.dao_main_f import DaoPosts, DaoComments, DaoBookmarks
from configs.config import PATH_JSON_POSTS, PATH_JSON_COMMENTS, PATH_JSON_BOOKMARKS, LENGTH_CONTENT

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


def shorts_content_add_bookmark(posts_all):
    bookmarks = DaoBookmarks(PATH_JSON_BOOKMARKS)
    bookmarks = bookmarks.get_bookmarks_all()
    bookmarks_set = set()
    for bookmark_one in bookmarks:
        bookmarks_set.add(bookmark_one.get('post_id'))
    for post in posts_all:
        post['content'] = post['content'][0:LENGTH_CONTENT]
        post['bookmark'] = True if post['pk'] in bookmarks_set else False
    return posts_all, len(bookmarks_set)


def add_delete_bookmark(post_id):
    bookmarks = DaoBookmarks(PATH_JSON_BOOKMARKS)
    bookmarks_l = list(bookmarks.get_bookmarks_all())
    for bookmark_one in bookmarks_l:
        if int(post_id) == bookmark_one['post_id']:
            bookmarks_l.remove(bookmark_one)
            bookmarks.save_all(bookmarks_l)
            return
    bookmarks_l.append({'post_id': int(post_id)})
    bookmarks.save_all(bookmarks_l)


@blueprint_main.route('/', methods=['GET'])
def main_page():
    logging.info("index.html")
    posts_all = DaoPosts(PATH_JSON_POSTS)
    posts_all, count = shorts_content_add_bookmark(posts_all.get_posts_all())
    return render_template('index.html', posts=posts_all, count_bookmarks=count)


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
    posts_l, _ = shorts_content_add_bookmark(posts_o.get_posts_by_user(user_name))
    return render_template('user-feed.html', posts=posts_l)


@blueprint_main.route('/search/<search_str>')
def search_page(search_str):
    logging.info(f"/search/{search_str}")
    posts_o = DaoPosts(PATH_JSON_POSTS)
    posts_l, count = posts_o.search_for_posts(search_str)
    posts_l, _ = shorts_content_add_bookmark(posts_l)
    return render_template('search.html', posts=posts_l, count=count)


@blueprint_main.route('/search/', methods=['GET'])
def search_page_request():
    posts_o = DaoPosts(PATH_JSON_POSTS)
    search_str = request.values.get('search')
    logging.info(f"/search/?search={search_str}")
    posts_l, count = posts_o.search_for_posts(search_str)
    posts_l, _ = shorts_content_add_bookmark(posts_l)
    return render_template('search.html', posts=posts_l, count=count)


@blueprint_main.route('/tag/<tag_name>')
def tag_page(tag_name):
    logging.info(f"/tag/{tag_name}")
    posts_o = DaoPosts(PATH_JSON_POSTS)
    posts_l, count = posts_o.search_for_posts(f'#{tag_name}')
    posts_l, _ = shorts_content_add_bookmark(posts_l)
    return render_template('tag.html', posts=posts_l, tag_name=tag_name)


@blueprint_main.route('/bookmarks/')
def bookmarks_page():
    logging.info("/bookmarks/")
    post = DaoPosts(PATH_JSON_POSTS)
    bookmarks = DaoBookmarks(PATH_JSON_BOOKMARKS)
    bookmarks = bookmarks.get_bookmarks_all()
    posts_all = []
    for bookmark_one in bookmarks:
        pk = bookmark_one.get('post_id')
        posts_temp = post.get_post_by_pk(pk)
        posts_temp['content'] = posts_temp['content'][0:LENGTH_CONTENT]
        posts_temp['bookmark'] = True
        posts_all.append(posts_temp)
    return render_template('bookmarks.html', posts=posts_all)


@blueprint_main.route('/bookmarks/add/<int:post_id>')
def bookmarks_add_page(post_id):
    logging.info(f'bookmarks_add_page {post_id}')
    add_delete_bookmark(post_id)
    return redirect('/', code=302)


@blueprint_main.route('/bookmarks/delete/<int:post_id>')
def bookmarks_delete_page(post_id):
    logging.info(f'bookmarks_delete_page {post_id}')
    add_delete_bookmark(post_id)
    return redirect('/', code=302)
