import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
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


