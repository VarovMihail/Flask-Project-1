from flask import jsonify
from flask import Flask

app = Flask('app')


class ApiException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message


@app.errorhandler(ApiException)
def error_handler(error: ApiException):
    response = jsonify({
        'status': 'error',
        'message': error.message
    })
    response.status_code = error.status_code
    return response
