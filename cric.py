import sqlite3

con = sqlite3.connect('cric-data.db')
cur = con.cursor()

print('\nKohli''s stats:-\n')
year = 2016
for row in cur.execute('SELECT `Batting Average`, `Batting Strike Rate`, `Highest Score` FROM ipl WHERE Player = "V Kohli"'):
    print(year)
    print('avg:',row[0],' ','sr:',row[1],' ','hs:',row[2])
    year = year + 1

print('\nPant''s stats:-\n')
year = 2016
for row in cur.execute('SELECT `Batting Average`, `Batting Strike Rate`, `Highest Score` FROM ipl WHERE Player = "RR Pant"'):
    print(year)
    print('avg:',row[0],' ','sr:',row[1],' ','hs:',row[2])
    year = year + 1
print('\n')
con.commit()
con.close()