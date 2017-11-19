from flask import Flask, redirect, url_for, session
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
   		session['username'] = request.form['username']
   		password = request.form['password']
   		if(dbHandler.checkUser(session['username'],password)):
   			return redirect(url_for('dash'))
   		dbHandler.insertUser(session['username'], password)
   		users = dbHandler.retrieveUsers()
		return render_template('index.html', users=users)
   	else:
   		return render_template('index.html')

@app.route('/user')
def dash():
	if 'username' in session:
		return 'User %s'%session['username']
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
