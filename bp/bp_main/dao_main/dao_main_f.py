#
# get_comments_by„post_id(post_id) - возвращает комментарии определенного поста.
# Функция должна вызывать ошибку ValueError если такого поста нет и пустой список, если у
# поста нет комментов.
#
# search_for_posts(query) - возвращает список постов по ключевому слову
import json


class DaoMain:
    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        """return all posts"""
        with open(self.path, 'r', encoding='UTF-8') as fp:
            return json.load(fp)

    def get_posts_by_user(self, user_name: str) -> list:
        """It's returns posts by a specific user. Feature must return valueError if such a user does not exist and
        empty list if user does not have posts"""
        post_return: list
        post_all = self.get_posts_all()
        for post in post_all:
            if user_name.lower() == post['poster_name']:
                post_return.append(post)
        return post_return

    def get_post_by_pk(self, pk):
        """ get_post_by_pk(pk)  возвращает один пост по его идентификатору."""
