import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    birth_date = Column(Date, nullable=False)

class UserInputs(Base):
    __tablename__ = 'user_inputs'
    id = Column(Integer, primary_key=True)
    login = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)


class Database:
    def __init__(self, url):
        self.engine = create_engine(url)
        Base.metadata.create_all(bind=self.engine)

    def add_user_inputs(self, user_inputs):
        session = sessionmaker(bind=self.engine)()
        session.add(user_inputs)
        session.commit()
        session.close()

    def add_user(self, user):
        session = sessionmaker(bind=self.engine)()
        session.add(user)
        session.commit()
        session.close()

    def get_user(self, user_id):
        session = sessionmaker(bind=self.engine)()
        user = session.query(User).filter(User.id == user_id).first()
        session.close()
        return user

    def delete_user(self, user_id):
        session = sessionmaker(bind=self.engine)()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()

