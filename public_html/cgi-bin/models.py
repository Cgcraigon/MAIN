# -*- coding: iso-8859-1 -*-
'''Classes to represent our gene expression objects'''
#Imports the MySQL module.
import MySQLdb
# a class that allows me to store my MySQL information so that the script can do its function. 
class DBHandler():
    '''The static database connection - avoids overuse of resources'''
    connection=None
    dbname='cgcraigon'
    dbuser='cgcraigon'
    dbpassword='sFv9iwKj'
    # Defining a function that will log into MySQL when the script is being executed - uses information from class DBHandler above.
    def __init__(self):
        if DBHandler.connection == None:
            DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname,user=DBHandler.dbuser, passwd=DBHandler.dbpassword)
    def cursor(self):
	return DBHandler.connection.cursor()
# This class will store output from the query done on MySQL
class Gene():
    Gene_ID=''
    Gene_Accession=''
    Gene_Descript=''
    probelist=[]
    # this function runs a query search to MySQL.
    def __init__(self,geneid):
    	#logs into MySQL
        db=DBHandler()
	cursor=db.cursor()
	# the query search that will be posed to MySQL
	sql='SELECT Gene_Accession, Gene_Descript from Gene where Gene_ID=%s'
	self.gene_id=geneid
	cursor.execute(sql,(geneid,))    
	#retrieves results and then fills the class feilds.
	result=cursor.fetchone()
	self.gene_title	=result[0]
        self.gene_symbol=result[1]
        # now searching for the probes 
        probesql='SELECT ID_REF from Probes where Gene_ID=%s'
        cursor.execute(probesql,(geneid,))
        # fills the probes list 
        for result in cursor.fetchall():
		print '%s'%result
        self.probelist.append(result[0])
    
