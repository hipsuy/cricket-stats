import sqlite3

con = sqlite3.connect('cric-data.db')
cur = con.cursor()

print('IPL STATS')

while True:
    option = int(input('\n\n1. Batting stats\n2. Bowling stats\n3. quit\n\t=>Choose option: '))
    if option == 1:
        while True:
            name = (input('\nBATTING STATS\nEnter player name or enter 0 to go back to main menu: '), )
            if name[0] == '0':
                break
            print('\nSeason\t\tMatches\t\tRuns\t\tAvg\t\tSR\t\tHS')

            for row in cur.execute('SELECT Tournament, `Matches`, `Runds Scored`, `Batting Average`, `Batting Strike Rate`, `Highest Score` FROM ipl WHERE Player = ? ORDER BY Tournament', name):
                print(f'{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3].split(".")[0]}\t\t{(row[4]).split(".")[0]}\t\t{row[5]}')


    elif option == 3:
        print('BYE!')
        break        

print('\n')
con.commit()
con.close()