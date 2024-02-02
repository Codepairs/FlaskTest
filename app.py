from flask import render_template, Flask, request
from datetime import datetime

import templates.database

app = Flask(__name__)

class FlaskPoweredServer:
    def __init__(self):
        self.db: templates.database.Database|None = None
        self.app = app
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SQL_gfccdjhl1@localhost:5432/test'

        @self.app.route('/')
        def starting_page():
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return render_template('index.html', current_time=current_time)

        @app.route('/test', methods=['GET', 'POST'])
        def authorization():

            if request.method == 'POST':
                Login = request.form.get('Login')
                Password = request.form.get('Password')
                print(Login, Password)
                self.db.insert_time(Password)
                self.db.selection_query()

                if Login == "admin" and Password == "admin":
                    return "Correct"
                else:
                    return "Incorrect"

            return '''
                     <form method="POST">
                         <div><label>Login: <input type="text" name="Login"></label></div>
                         <div><label>Password: <input type="text" name="Password"></label></div>
                         <input type="submit" value="Enter">
                     </form>'''


    def run(self, debug_mode=True):
        self.app.run(debug=debug_mode)

    def set_db(self, db):
        self.db = db

