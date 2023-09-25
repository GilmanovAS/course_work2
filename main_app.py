from flask import Flask
from bp.bp_main.main_view import blueprint_main

app = Flask(__name__)
app.config.from_pyfile('configs/config.py')

app.register_blueprint(blueprint_main)


@app.errorhandler(404)
def page_not_found(error):
    return "Page not found", 404


@app.errorhandler(500)
def special_exception_handler(error):
    return 'Database connection failed', 500


if __name__ == '__main__':
    app.run()
