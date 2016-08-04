from app import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(200))
	timestamp = db.Column(db.DateTime)

	def __repr__(self):
		return '<Post %r>' % (self.body)