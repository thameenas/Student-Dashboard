from flask import Flask, redirect, url_for, session
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

app.jinja_env.globals.update(findUserName=dbHandler.findUserName) 

def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method=='POST':
   		username = request.form['username']
   		if(dbHandler.checkUser(username,password)):
   			session['username']=username
   			return redirect(url_for('dash'))
   		
   		#dbHandler.insertUser(session['username'], password)
   		users = dbHandler.retrieveUsers()
		return render_template('index.html', users=users)
   	else:
   		return render_template('index.html')

@app.route('/user', methods=['GET','POST'])
def dash():
	if 'username' in session:
		subjects=dbHandler.retrievesubs()
		print subjects

		return render_template('dashboard.html', username=session['username'], subject=subjects)


@app.route('/createnew', methods=['POST','GET'])
def createnew():
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']


		#userlist=dbHandler.retrieveUsers()
		#if username in userlist[0]:
		#	return redirect(url_for('createnew'))
		session['username']=username
		dbHandler.insertUser(username,password)
		return redirect(url_for('home'))
	else:
		return render_template('new.html')

@app.route('/create',methods=['POST','GET'])
def subcreate():
	if request.method=='POST':
		subject=request.form['subject']
		
		dbHandler.addsubject(subject)
		return redirect(url_for('dash'))
	else:
		return render_template('createsub.html')

@app.route('/topic/<subid>',methods=['GET','POST'])
def topic(subid):
	messages=dbHandler.retrievemsg(subid)
	dbHandler.retrievemsg2(subid)
	return render_template('topic.html',messages=messages,subid=subid)


@app.route('/topic/<subid>/new',methods=['GET','POST'])
def newmessage(subid):
	if request.method=='POST':
		message=request.form['message']
		userId=dbHandler.findUserId(session['username'])
		print userId, subid
		dbHandler.addmsg(message,subid,userId[0])
		return redirect(url_for('.topic',subid=subid))
	else:	
		return render_template('newmessage.html',subid=subid)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
