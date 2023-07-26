import mysql.connector

class DBCollectionFile:
    def debconnect(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Harsh@123", database='pythonmaybatch1')
        #conn=mysql.connector.connect(host="localhost",user="root",password="123456",database="pythonmaybatch")
        print(conn)
        mycursor=conn.cursor()
        mycursor.execute("select * from project")
        data=mycursor.fetchall()
        return data