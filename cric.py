import sqlite3

con = sqlite3.connect('cric-data.db')
cur = con.cursor()

print('\nKohli''s average and strike rate over the years:-\n')
year = 2016
i = 0
for row in cur.execute('SELECT `Batting Average`, `Batting Strike Rate` FROM ipl WHERE Player = "V Kohli"'):
    print(year+ i)
    print('avg:',row[0],' ','sr:',row[1],'\n')
    i = i + 1
print('\n')
con.commit()
con.close()