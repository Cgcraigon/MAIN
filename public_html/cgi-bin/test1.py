#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
chmod +x test1.py

import cgi
import cgitb
import os
from mod_python import apache 
module = apache.import_module('models.py', path =[directory])

cgitb.enable()

form = cgi.FieldStorage()

Gene = models.Gene([query])
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)

print "<table>"

print "</body></html>"
