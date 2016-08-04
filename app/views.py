from flask import Flask, render_template, flash, redirect, session, url_for, request, g
from datetime import datetime
from app import app, db
from .forms import PostForm
from .models import Post

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(id=app.id(), body=form.post.data, timestamp=datetime.utcnow())
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('index'))
	posts = Post.query.all()
	return render_template('index.html',
							title = 'Přehled poznámek',
							form=form,
							posts=posts)

@app.route('/notes')
def notes():
	posts = Post.query.all()
	return render_template('notes.html',
							title = 'Přidat poznámku',
						   posts=posts)

@app.route('/calendar')
def calendar():
	user = {'nickname': 'User'}
	return render_template('calendar.html',
							title = 'Kalendář',
							user=user)

