from flask import Flask
from views import my_view

app = Flask(__name__)
app.register_blueprint(my_view)
app.config.from_pyfile('config.py')


if __name__ == '__main__':
    app.run()
