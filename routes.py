from app import app
@app.route('/')
@app.route('/index')
def index():
	user = 'Cala'
return render_template('index.html', user=user)
    
