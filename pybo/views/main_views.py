from flask import Blueprint, url_for
from werkzeug.utils import redirect

#블루프린트 객체 생성
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

