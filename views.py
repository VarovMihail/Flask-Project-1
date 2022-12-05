from flask import request
from flask.views import MethodView
from flask import jsonify

from errors import ApiException
from models import Session, User, Advertisement


def hello_word():
    return 'Hello Word!'


class UserView(MethodView):
    def get(self, user_id):
        with Session() as session:
            user = session.query(User).get(user_id)
            if user is None:
                raise ApiException
            print(f'{user} = ')
            return jsonify({
                'id': user.id,
                'email': user.email
            })

    def post(self):
        with Session() as session:
            data = request.json
            new_user = User(**data)
            session.add(new_user)
            session.commit()
            return jsonify({'id': new_user.id, 'email': new_user.email})

    def delete(self, user_id):
        with Session() as session:
            user = session.query(User).get(user_id)
            session.delete(user)
            session.commit()
            return jsonify({'status': 'deleted'})


class AdvView(MethodView):
    def get(self, adv_id):
        with Session() as session:
            adv = session.query(Advertisement).get(adv_id)
            return jsonify({
                'id': adv.id,
                'title': adv.title,
                'description': adv.description,
                'user_id': adv.user_id,
                # 'author': adv.author,
            })

    def post(self):
        with Session() as session:
            data = request.json
            adv = Advertisement(**data)
            session.add(adv)
            session.commit()
            return jsonify({
                'title': adv.title,
                'description': adv.description,
                'user_id': adv.user_id,
            })

    def delete(self, adv_id):
        with Session() as session:
            adv = session.query(Advertisement).get(adv_id)
            session.delete(adv)
            session.commit()
            return jsonify({'status': 'deleted'})
