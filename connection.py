import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
mycur = mydb.cursor()
mycur.execute("show databases")
mysh = mycur.fetchone()
for i in mysh:
    print(i)