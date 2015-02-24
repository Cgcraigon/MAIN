# -*- coding: iso-8859-1 -*-
'''Classes to represent our gene expression objects'''

import MySQLdb
#Incomplete outline script for a database interacting class to represent a gene.

class DBHandler():
    '''The static database connection - avoids overuse of resources'''
    connection=None
    dbname='cgcraigon'
    dbuser='cgcraigon'
    dbpassword='sFv9iwKj'
    def __init__(self):
        if DBHandler.connection == None:
            DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname,user=DBHandler.dbuser, passwd=DBHandler.dbpassword)
    
    def cursor(self):
	return DBHandler.connection.cursor()

class Gene():
    gene_symbol=''
    gene_title=''
    gene_id=''
    probelist=[]
    def __init__(self,geneid):
	self.gene_id=geneid
        db=DBHandler()
	cursor=db.cursor()
	sql='SELECT gene_title, gene_symbol  from gene where gene_id=%s'
	cursor.execute(sql,(geneid,))    
	result=cursor.fetchone()
	self.gene_title	=result[0]
        self.gene_symbol=result[1]
        probesql='SELECT probeid from probe where geneid=%s'
        cursor.execute(probesql,(geneid,))
        for result in cursor.fetchall():
		print '%s'%result
        self.probelist.append(result[0])
    def get_expression(self,experiment):
    	db=DBHandler()
    	cursor=db.cursor()
    	sql='SELECT expression where ID_REF=%s AND Sample_ID=%s'
    	print("Complete")
