from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db, success_stories
from myapp.models import SuccessStory
from myapp.success_stories.forms import SuccessStoryForm

success_stories = Blueprint('blog_posts', __name__)


