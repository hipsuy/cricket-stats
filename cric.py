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
    elif option == 2:
        while True:
            name = input('\nBOWLING STATS\nEnter player name or enter 0 to go back to main menu: ')
            if name == '0':
                break
            print('\nSeason\t\tMatches\t\tWickets\t\tAvg\t\tSR\t\tEco\t\tBB')

            for row in cur.execute('SELECT Tournament, Matches, `Wickets Taken`,`Bowling Average`,`Bowling Strike Rate`, `Bowling Economy Rate`,`Best Bowling Figures` FROM ipl WHERE Player = ? ORDER BY Tournament',(name, )):
                print(f'{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3].split(".")[0]}\t\t{row[4].split(".")[0]}\t\t{row[5]}\t\t{row[6]}')
    elif option == 3:
        print('BYE!')
        break        

con.commit()
con.close()