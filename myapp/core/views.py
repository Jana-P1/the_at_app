# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import SuccessStory

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    success_stories = SuccessStory.query.order_by(SuccessStory.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', success_stories=success_stories)

@core.route('/info')
def info():
    return render_template('info.html')