import sqlite3 as sql
#
con = sql.connect("database.db")
cursor = con.cursor()
con.execute("CREATE TABLE IF NOT EXISTS helper (ques INT PRIMARY KEY NOT NULL, ans TEXT NOT NULL);")
# lis = '0ABCDEFGHIJKL'
# for i in range(1,10):
#     cursor.execute(f'Select * from helper where ques = {i}')
#     r = cursor.fetchall()
#     if not r:
#         con.execute(f"INSERT INTO helper (ques,ans) VALUES ({i},'{lis[i]}')")
# con.commit()
# # con.execute("INSERT INTO helper (ques,ans) VALUES (1,'A')")
cur = con.execute("Select * from helper")
for i in cur:
    print(i)
con.close()


def supplier(val):
    val_list = val.split(':')
    q, a = int(val_list[0]), val_list[1]
    con = sql.connect("database.db")
    cursor = con.cursor()
    cursor.execute(f'Select * from helper where ques = {q}')
    r = cursor.fetchall()
    if r:
        con.execute(f"DELETE FROM Helper WHERE ques = {q}")
    con.execute(f"INSERT INTO helper (ques,ans) VALUES ({q},'{a}')")
    con.commit()
    con.close()


def destroyer():
    con = sql.connect("database.db")
    con.execute("DELETE FROM helper")
    con.commit()
    con.close()
