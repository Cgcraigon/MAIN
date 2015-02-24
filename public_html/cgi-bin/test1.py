#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import cgi
import cgitb
import os
from mod_python import apache 
dirctory = os.path.dirname(__models.py__)
module = apache.import_module('models.py', path=[directory])
cgitb.enable()
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"
form = cgi.FieldStorage()
db=models.DBHandler()
cursor=db.cursor()
cursor.execute('select id_ref from probe where gene_is=%s',(form['query'],))

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)

print "<table>"

print "</body></html>"
