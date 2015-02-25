#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
#Imports cgi modules 
import cgi
import cgitb#
#imports models.py 
import models
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
