import sqlite3

def search(word):
	word=word.capitalize()
	conn=sqlite3.connect("dict.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM Dictionary WHERE word=?",(word,))
	rows=cur.fetchall()
	conn.close()
	return(rows)
	
print(search("rain"))