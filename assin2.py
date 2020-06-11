import sqlite3

conn= sqlite3.connect('cap15.sqlite')
cur= conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

file= 'mbox.txt'
file = open(file)

for line in file:
    if not line.startswith('From: '): continue
    pieces= line.split()
    org=pieces[1].split('@')
    org=org[1]
    #print(org)
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org,count) VALUES (?,1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()

sql= 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sql):
    print(row)

cur.close()
