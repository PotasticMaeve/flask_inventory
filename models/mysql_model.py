""" Model untuk Database Mysql """

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "claudia",
    passwd = "claudia12",
    database = "db_flaskbasic"
)

def insert_user(username, password):
    cursor = con.cursor(prepared=True)
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",(username, password))
    con.commit()

def select_user():
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(result)

def update_user(username,password,id):
    cursor = con.cursor(prepared=True)
    cursor.execute("UPDATE users SET username = ?,password = ? WHERE id = ?",(username,password,id))
    con.commit()
    return cursor.rowcount, "record(s) affected"

def delete_user(id):
    cursor = con.cursor(prepared=True)
    cursor.execute("DELETE FROM users WHERE id = ? ",(id))
    con.commit()
    return cursor.rowcount, "record(s) deleted"
    
def data_checking(username, password):
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = '{}' and password = '{}'".format(username, password))
    result = cursor.fetchall()
    if len(result) > 0:
        return 1
    else:
        return 0

