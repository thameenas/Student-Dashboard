import sqlite3 as sql

def insertUser(email,username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (email,username,password) VALUES (?,?,?)", (email,username,password))
    con.commit()
    con.close()
def checkUser(username,password):
	con=sql.connect("database.db")
	cur=con.cursor()
	cur.execute("SELECT password from users where username=?",(username,))
	print "checking user"
	cred=cur.fetchone()
	print cred
	con.close()
	if cred is not None:
		if password==cred[0]:
			return 1
	return 0
def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users
def findUserId(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT id FROM users where username=?",(username,))
	users = cur.fetchone()
	con.close()
	return users
def findUserName(userId):

	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username FROM users where id=?",(userId,))
	users = cur.fetchone()
	con.close()
	return users

def retrievepass(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT password FROM users where username=?",(username,))
	password = cur.fetchone()
	con.close()
	return password[0]

def addpass(username,newpass):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("UPDATE users SET password=? where username=?",(newpass,username))
	con.commit()
	con.close()

def addsubject(name):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT into subject (name) VALUES (?)",(name,))
	con.commit()
	con.close()
	
def retrievesubs():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM subject")
	subjects = cur.fetchall()
	con.close()
	return subjects

def addmsg(message,subjectid,userid):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT into messages (subid,userid,message) VALUES (?,?,?)",(subjectid,userid,message,))
	con.commit()
	con.close()

def retrievemsg(subjectid):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM messages where subid=?",(int(subjectid),))
	messages = cur.fetchall()
	con.close()
	print messages
	return messages

def retrievemsg2(subjectid):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT id FROM messages WHERE subid=?",(subjectid,))
	messages = cur.fetchall()
	con.close()
	print "MEASS"
	print messages 
	return messages