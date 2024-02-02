from flask import render_template, Flask, request
from datetime import datetime

import templates.database

app = Flask(__name__)
host = 'localhost'
port = '5432'
user = 'postgres'
password = '123'
name = 'test'
url = f'postgresql://{user}:{password}@{host}:{port}/{name}'
db = templates.database.Database(url)


class FlaskPoweredServer:
    def __init__(self):
        self.db: templates.database.Database | None = None

        @app.route('/')
        def starting_page():
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return render_template('index.html', current_time=current_time)

        @app.route('/test', methods=['GET', 'POST'])
        def authorization():

            if request.method == 'POST':
                login = request.form.get('Login')
                password = request.form.get('Password')
                ###ЖЕСТКАЯ ПРИКРУТКА БД
                print(login, password)
                self.db.add_user_inputs(templates.database.UserInputs(id=1, login=login, password=password))
                ###ЖЕСТКО РАБОТАЕТ

                if login == "admin" and password == "admin":
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
        app.run(debug=debug_mode)

    def set_db(self, db):
        self.db = db
