from models import Base, Session, User, Advertisement
from pytest import fixture
import time


@fixture(scope='session', autouse=True)  # выполнить автоматически 1 раз за сессию
def prepare_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()


@fixture()
def create_user():
    with Session() as session:
        user = User(email=f'{time.time()}@mail.ru', password='123')
        session.add(user)
        session.commit()
        return {
            'id': user.id,
            'email': user.email
        }


@fixture()
def create_advertisement(create_user):
    with Session() as session:
        adv = Advertisement(
            title='test_title',
            description='short_description',
            user_id=create_user['id'],
        )
        session.add(adv)
        session.commit()
        return {
            'id': adv.id,
            'title': adv.title,
            'description': adv.description,
            'user_id': adv.user_id,
            'author': adv.author,
        }
