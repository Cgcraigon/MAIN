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
            DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, \
user=DBHandler.dbuser, passwd=DBHandler.dbpassword)

    def cursor(self):
	return DBHandler.connection.cursor()

class Gene():
    '''A class that describes an individual gene'''
    gene_symbol=''
    gene_title=''
    gene_id=''
    probelist=[]

    def __init__(self,geneid):
        '''Init method for Gene'''
	self.gene_id=geneid
        db=DBHandler()
	cursor=db.cursor()
	sql='select gene_title, gene_symbol from gene where gene_id=%s'
	cursor.execute(sql,(geneid,))
	    #query database
	    #get result and populate the class fields.
	result=cursor.fetchone()
	self.gene_title	=result[0]
        self.gene_symbol=result[1]
        #now fetch the probes..
        probesql='select probeid from probe where geneid=%s'
	#fill in the blanks yourself


	for result in cursor.fetchall():
  	    self.probelist.append(result[0])

    def get_expression(self,experiment):
		'''Retrieve expression values for a given experiment for this gene'''
		#TODO
