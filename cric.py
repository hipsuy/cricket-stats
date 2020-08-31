import sqlite3

con = sqlite3.connect('cric-data.db')
cur = con.cursor()




con.commit()
con.close()