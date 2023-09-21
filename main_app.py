from flask import Flask
from bp.bp_main.main_view import blueprint_main

app = Flask(__name__)
app.config.from_pyfile('configs/config.py')

app.register_blueprint(blueprint_main)

if __name__ == '__main__':
    app.run()
