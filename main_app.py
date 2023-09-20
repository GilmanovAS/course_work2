from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_pyfile('config.py')


@app.route('/')
def root_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
