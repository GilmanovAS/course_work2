import json


class DaoPosts:
    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        """return all posts"""
        with open(self.path, 'r', encoding='UTF-8') as fp:
            return json.load(fp)

    def get_posts_by_user(self, user_name: str) -> list:
        """It's returns posts by a specific user. Feature must return valueError if such a user does not exist and
        empty list if user does not have posts"""
        post_return = []
        post_all = self.get_posts_all()
        for post in post_all:
            if user_name.lower() == post['poster_name'].lower():
                post_return.append(post)
        return post_return

    def get_post_by_pk(self, pk: int) -> None:
        """ get_post_by_pk(pk)  возвращает один пост по его идентификатору."""
        post_all = self.get_posts_all()
        for post in post_all:
            if pk == post['pk']:
                return post

    def search_for_posts(self, search_str):
        """возвращает список постов по ключевому слову"""
        post_return = []
        post_all = self.get_posts_all()
        count = 0
        for post in post_all:
            if search_str.lower() in post['content'].lower():
                post_return.append(post)
                count += 1
        return post_return, count


class DaoComments:
    def __init__(self, path):
        self.path = path

    def get_comments_all(self):
        """return all comments"""
        with open(self.path, 'r', encoding='UTF-8') as fp:
            return json.load(fp)

    def get_comments_by_post_id(self, post_id):
        # get_comments_by„post_id(post_id) - возвращает комментарии определенного поста.
        # Функция должна вызывать ошибку ValueError если такого поста нет и пустой список, если у
        # поста нет комментов.
        return_comments = []
        count = 0
        comments_all = self.get_comments_all()
        for comment in comments_all:
            if post_id == comment['post_id']:
                return_comments.append(comment)
                count += 1
        return return_comments, count


class DaoBookmarks:
    def __init__(self, path):
        self.path = path

    def get_bookmarks_all(self):
        """return all comments"""
        with open(self.path, 'r', encoding='UTF-8') as fp:
            return json.load(fp)

    def get_bookmarks_by_post_id(self, post_id):
        # get_comments_by„post_id(post_id) - возвращает комментарии определенного поста.
        # Функция должна вызывать ошибку ValueError если такого поста нет и пустой список, если у
        # поста нет комментов.
        bookmarks_all = self.get_bookmarks_all()
        for bookmark in bookmarks_all:
            if post_id == bookmark['post_id']:
                return bookmark
