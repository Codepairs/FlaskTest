#export FLASK_RUN_PORT=5050

from app import *
from templates.database import Database


if __name__ == '__main__':
    app = FlaskPoweredServer()
    db = Database()
    db.create_table()
    db.check_connection()
    app.set_db(db)
    app.run(debug_mode=True)

