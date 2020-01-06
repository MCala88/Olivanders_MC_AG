from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
	user = 'Cala'
	if (user):
		return render_template('index.html', user=user)
	else:
		return render_template('index.html')



    
