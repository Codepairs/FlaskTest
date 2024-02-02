import sqlalchemy

#%load_ext sql
from sqlalchemy import create_engine

class Database:
    def __init__(self):
        self._engine = create_engine('postgresql://postgres:SQL_gfccdjhl1@localhost:5432/test')
        self._connection = self._engine.connect()
        self._connection.execute(sqlalchemy.text(
            '''
            DROP TABLE IF EXISTS time_db;

            CREATE TABLE time_db (
                    id SERIAL PRIMARY KEY,
                    time VARCHAR(30) NOT NULL
                    );
            '''
        ))


    def create_table(self):
        self._engine = create_engine('postgresql://postgres:SQL_gfccdjhl1@localhost:5432/test')
        self._connection = self._engine.connect()
        self._connection.execute(sqlalchemy.text(
            '''
            DROP TABLE IF EXISTS time_db;

            CREATE TABLE time_db (
                    id SERIAL PRIMARY KEY,
                    time VARCHAR(30) NOT NULL
                    );
            '''
        ))

    def check_connection(self):
        print(self._connection)

    def selection_query(self, query = "SELECT * FROM time_db;"):
        result = self._connection.execute(sqlalchemy.text(query)).fetchall()
        print(result)

    def insert_time(self, time: str):
        self._connection.execute(sqlalchemy.text(
            '''
            INSERT INTO time_db (time)
            VALUES ('{0}');
            '''.format(time)
        ))
        print(self._connection)

if __name__=="__main__":
    db = Database()
    db.check_connection()
    db.insert_time("21:47:15")
    db.selection_query()

#my_query = ''
#results = connection.execute(text("SELECT * FROM users")).fetchall()