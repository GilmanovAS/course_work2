import logging

from flask import Flask

from bp.bp_api.api_json import blueprint_api
from bp.bp_main.main_view import blueprint_main

app = Flask(__name__)
app.config.from_pyfile('configs/config.py')
logging.basicConfig(filename='api.log', level=app.config.get('LEVEL_LOG'),
                    format='%(asctime)s [%(levelname)s] %(message)s')

app.register_blueprint(blueprint_main)
app.register_blueprint(blueprint_api)


@app.errorhandler(404)
def page_not_found(error):
    logging.info("Page not found")
    return "Page not found", 404


@app.errorhandler(500)
def special_exception_handler(error):
    return 'Database connection failed', 500


if __name__ == '__main__':
    app.run()
