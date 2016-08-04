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
		post = Post(body=form.post.data, timestamp=datetime.utcnow())
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('index'))
	posts = Post.query.all()
	return render_template('index.html',
							title = 'Přehled poznámek',
							form=form,
						   	db=db,
							posts=posts)

@app.route('/add')
def add():
	user = {'nickname': 'User'}
	return render_template('add.html',
							title = 'Přidat poznámku',
							user=user)

@app.route('/calendar')
def calendar():
	user = {'nickname': 'User'}
	return render_template('calendar.html',
							title = 'Kalendář',
							user=user)

