#!usr/bin/python
# -*- coding: iso-8859-1 -*-

import MySQLdb
db=MySQLdb.connect(db="cgcraigon",user="cgcraigon",passwd="sFv9iwKj")
cursor=db.cursor()
cursor.execute("SELECT expression FROM expression where expression =%s")
result=cursor.fetchall()
print result