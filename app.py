from flask import render_template, Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class FlaskPoweredServer:
    def __init__(self):
        self.db = db
        self.app = app
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/base.db'

        @self.app.route('/')
        def starting_page():
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return render_template('index.html', current_time=current_time)

    def run(self, debug_mode=True):
        self.app.run(debug=debug_mode)

