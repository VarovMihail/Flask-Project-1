import sqlalchemy
from flask import Flask

from views import hello_word, UserView, AdvView

app = Flask('app')

app.add_url_rule('/hw/', view_func=hello_word, methods=['get'])
app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users'), methods=['get', 'delete'])
app.add_url_rule('/users/', view_func=UserView.as_view('users_create'), methods=['post'])
app.add_url_rule('/advertisements/', view_func=AdvView.as_view('advertisement_create'), methods=['post'])
app.add_url_rule('/advertisements/<int:adv_id>', view_func=AdvView.as_view('advertisements'), methods=['get', 'delete'])

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
