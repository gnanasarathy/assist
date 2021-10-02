import sqlite3 as sql


def reading():
    con = sql.connect('database.db')
    cursor = con.cursor()
    cursor.execute("Select * from helper")
    result = cursor.fetchall()
    if len(result) == 0:
        p = "Currently it is Empty!!!"
    else:
        p = "Ques\tOption\n"
        result.sort(key=lambda n: n[0])
        for row in result:
            p += str(row[0]) + '\t' + row[1].upper() + '\n'
    return p
