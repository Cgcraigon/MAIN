#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#Imports cgi modules 
import cgi
import cgitb#
#imports models.py 
#import models
cgitb.enable()
form = cgi.FieldStorage()
import MySQLdb
sql="SELECT Gene_Accesion, Gene_Descript FROM Gene where Gene_ID=%s"
db=MySQLdb.connect(db='cgcraigon',user='cgcraigon',passwd='sFv9iwKj')
cursor=db.cursor()
cursor.execute(sql,form[''].value)
result=cursor.fetchall()
result

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script Output</TITLE></head>"
print "<body><H1>Sample Information</H1>"
print "<b>Gene ID        :</b>"

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)
# Prints the table
print "<table>"
print "<b> Gene_Accesion, Gene_Description<b>"
print result
print "</body></html>"
