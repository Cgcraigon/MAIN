#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import MySQldb
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)


db=MySQldb.connect(db="cgcraigon",user="cgcraigon",passwd="sFv9iwKj")
cursor=db.cursor()
cursor.execute()
result=cursor.fetchall()
print result

print "</body></html>"