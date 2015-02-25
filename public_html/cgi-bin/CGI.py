#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
chmod +x CGI.py
#Imports cgi modules 
import cgi
import cgitb
#Imports os module required for use with apache. 
import os
#imports apache 
from mod_python import apache 
# links the CGI.py with the models.py for importing information the website. 
dirctory = os.path.dirname(__models.py__)
module = apache.import_module('models.py', path=[directory])
cgitb.enable()
form = cgi.FeildStorage()
#creates a form where the output can be stored.
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<html><head><TITLE>CGI script output</TITLE></head>"
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"
for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k].value)
# Prints the table
print "<table>"

print "</body></html>"
