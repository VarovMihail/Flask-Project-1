import os
import datetime
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from db_config import DSN

engine = sq.create_engine(DSN, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    email = sq.Column(sq.String(length=50), unique=True, nullable=True)
    password = sq.Column(sq.String(length=50), nullable=False)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.email, self.password)


class Advertisement(Base):
    __tablename__ = 'Advertisements'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    title = sq.Column(sq.String(length=50), nullable=False)
    description = sq.Column(sq.String(length=100), nullable=False)
    created = sq.Column(sq.DateTime, default=datetime.datetime.now())
    user_id = sq.Column(sq.Integer, sq.ForeignKey('users.id'), nullable=False)
    author = relationship(User, backref='advertisements')


def create_tables():
    Base.metadata.drop_all()
    Base.metadata.create_all()


create_tables()
