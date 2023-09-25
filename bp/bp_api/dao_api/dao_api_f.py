import json


class DaoApi:
    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        """return all posts"""
        with open(self.path, 'r', encoding='UTF-8') as fp:
            return json.load(fp)

    def get_post_by_pk(self, pk: int) -> None:
        """ get_post_by_pk(pk)  возвращает один пост по его идентификатору."""
        post_all = self.get_posts_all()
        for post in post_all:
            if pk == post['pk']:
                return post