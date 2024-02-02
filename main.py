from app import *
from templates.database import Database


if __name__ == '__main__':
    app = FlaskPoweredServer()
    app.run(debug_mode=True)
    db = Database()
    app.set_db(db)
