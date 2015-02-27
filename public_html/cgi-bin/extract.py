#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#Imports cgi modules 
import cgi
import cgitb
"""imports cgi traceback -important to all interacts MySQl and html"""
cgitb.enable()
form = cgi.FieldStorage()
""" stores form submissions """
import MySQLdb
"""imports MySQLdb"""
sql="SELECT Gene_Accesion, Gene_Descript FROM Gene where Gene_ID=%s"
""" Queries the Gene_Accesion, Gene_Descript"""
db=MySQLdb.connect(db='cgcraigon',user='cgcraigon',passwd='sFv9iwKj')
"""establishes the link to the MySQL database"""
cursor=db.cursor()
"""activates cursor""" 
cursor.execute(sql,form[''].value)
"""Executes it"""
result=cursor.fetchall()
result
"""Fetches the Results"""
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script Output</TITLE></head>"
print "<body><H1>Sample Information</H1>"
print "<b>Gene_ID:      </b>"
"""Layout once Information has been recieved"""

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)
# Prints the table
print "<table>"
print "<b> Gene_Accesion, Gene_Description<b>"
print result
print "</body></html>"
""" Prints the results of the query"""
