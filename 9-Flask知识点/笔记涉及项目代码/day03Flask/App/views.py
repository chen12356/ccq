from flask import Blueprint

blue = Blueprint('first',__name__)


@blue.route('/test/')
def test():
    return 'HELLO '