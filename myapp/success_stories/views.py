from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db, success_stories
from myapp.models import SuccessStory
from myapp.success_stories.forms import SuccessStoryForm

success_stories = Blueprint('success_stories', __name__)

# Creates Success Story
@success_stories.route('/create', methods=['GET', 'POST'])
@login_required
def create():
  form = SuccessStoryForm()
  if form.validate_on_submit():
    success_story = SuccessStory(
      title=form.title.data, 
      story=form.story.data, user_id=current_user.id
    )
    db.session.add(success_story)
    db.session.commit()
    flash('Your success story was created!')
    print('Success story was successfully added')
    return redirect(url_for('core.index'))
  return render_template('create_story.html', form=form)

# Show a success story
@success_stories.route('/<int:success_story_id>')
def success_story(success_story_id):
  success_story = SuccessStory.query.get_or_404(success_story_id)
  return render_template(
    'success_story.html', title=success_story.title, date=success_story.date, story=success_story
  )

# Update a success story
@success_stories.route('/<int:success_story_id>/update', methods=['GET', 'POST'])
@login_required
def update(success_story_id):
  success_story = SuccessStory.query.get_or_404(success_story_id)
  
  if success_story.author != current_user:
    abort(403)

  form = SuccessStoryForm()

  if form.validate_on_submit():
    success_story.title = form.title.data
    success_story.story = form.story.data
    db.session.commit()
    flash("Success Story Updated")
    return redirect(url_for('success_stories.success_story', success_story_id=success_story.id))
  
  elif request.method == 'GET':
    form.title.data = success_story.title
    form.story.data = success_story.story
  
  return render_template('create_story.html', title='Updating', form=form)

# Delete a success story
@success_stories.route('/<int:success_story_id>/delete', methods=["GET", "POST"])
@login_required
def delete(success_story_id):

  success_story = SuccessStory.query.get_or_404(success_story_id)
  if success_story.author != current_user:
    abort(403)
  
  db.session.delete(success_story)
  db.session.commit()
  flash('Success Story Deleted')
  return redirect(url_for('core.index'))


