#takes the raw data file and creates 4 text files that can each be loaded into a table in mySQL
#!/usr/bin/python

# step 1. open the data file


#step 2. read the first line and then read more lines while the line doesn't match a specific pattern
while : #need to complete this
    line=fh.readline()


header= fh.readline().strip()

#capture the column names
colnames={}
index=0
for title in header.split('\t'):
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1



#open our output files, one per table.

#defines which columns are to go in each output file. For samples it is the 3rd header until the gene title header and they will be separated by '\t'
genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']


def buildrow(row, fields):
	'''Creates a tab separated list of values according to the columns listed in fields
	row: a list of values
	fields: a list of columns. Only the values in row corresponding to the columns in fields are output
	returns: A string that is a tab separated list of values terminated with a newline
	'''
    newrow=[]
    for f in fields:
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"


	#creates the rows for the expression file, is slightly different because for each probe and experiment there are several gene expression values.
def build_expression(row, samples):
	'''Builds tab separated rows for expression data. For each of the samples listed 
	it generates a line with the probe id, sample id and expression value.
	row: a list of values
	samples: a list of column headings corresponding to the samples
	'''
    exprrows=[]
    for s in samples:
        newrow=[s,]
	newrow.append(row[int(colnames['ID_REF'])])
	newrow.append(row[int(colnames[s])])
	exprrows.append("\t".join(newrow))
    return "\n".join(exprrows)+"\n"
	
	
#initialise a counter to count how many probe rows were processed.    
#writes the data to the files 
for line in fh.readlines():
    try:
        if line[0]=='!':
            continue
        row=line.strip().split('\t')
        genefile.write(buildrow(row, genefields))
        probefile.write(buildrow(row,probefields))
        expressionfile.write(build_expression(row, samples))	
		#increment the row counter
    except:
		pass

#close the created files after the data has been writen to them

#print out a message to indicate success with outputting the data.



