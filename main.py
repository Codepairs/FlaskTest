from app import *

if __name__ == '__main__':
    app = FlaskPoweredServer()
    app.set_db(db)
    app.run(debug_mode=True)

