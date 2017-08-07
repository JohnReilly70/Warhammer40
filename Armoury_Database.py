import sqlite3

db_conn = sqlite3.connect('Armoury.db')

cursor = db_conn.cursor()

db_conn.execute("DROP TABLE IF EXISTS Armoury")

try:
    #--[Head, Chest, L Arm, R Arm, L Leg, R Leg]
    db_conn.execute('''
        CREATE TABLE Armoury
       (
       NAME TEXT NOT NULL,
       LOCATION_COVERED TEXT NOT NULL,
       LOCATION_COVERED_LIST_CSV TEXT NOT NULL ,
       REQ INT NOT NULL,
       RENOWN CHAR(30) NOT NULL);

       '''
                    )

    db_conn.commit()

except sqlite3.OperationalError:
    print("Table couldn't be Created")

Armoury = [

["Astartes Power Armour", "All", "8,10,10,10,10,10", 0, "-"],
["Astartes Artificer Armour", "All", "12,12,12,12,12,12", 60, "Hero"],
["Astartes Scout Armour", "Body,Arms", "0,6,6,6,0,0", 0, "-"],
["Astartes Terminator Armour", "All", "14,14,14,14,14,14", 100, "Famed"],
["Carapace Armour", "All", "6,6,6,6,6,6", 0, "-"],
["Flak Armour", "All", "4,4,4,4,4,4", 0, "-"]

]


#db_conn.execute("INSERT INTO Armoury (NAME,LOCATION_COVERED,LOCATION_COVERED_LIST_CSV,REQ,RENOWN) VALUES ({}, {}, {}, {}, {})").format(Armour[0], Armour[1], Armour[2], Armour[3], Armour[4], Armour[5])
db_conn.executemany("INSERT INTO Armoury (NAME, LOCATION_COVERED, LOCATION_COVERED_LIST_CSV, REQ, RENOWN) VALUES(?,?,?,?,?)", Armoury)


db_conn.commit()
