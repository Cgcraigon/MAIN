# -*- coding: iso-8859-1 -*-
#takes the raw data file and creates 4 text files that can each be loaded into a table in mySQL
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
"""opens the script dataset 'GDS2842_full.soft'"""
infile= 'GDS3842_full.soft'
fh= open(infile)
line= fh.readline()
"""read through the table until it identifies the column pattern."""
while line[:20] != '!dataset_table_begin':
    line=fh.readline()
header= fh.readline().strip()
#Defines the titles for each column 
colnames={}
"""Locates the Column Names"""
index=0
for title in header.split('\t'):
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1
"""open our output files, one per table.""""
genefile=open('genes.txt', 'w')
expressionfile=open('expression.txt','w')
probefile=open('probes.txt', 'w')
"""Assigns the feild names that correspond table columns"""
genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']
"""# creates a row with the column headers""" 
def buildrow(row, fields):
    newrow=[]
    for f in fields:
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"
    """adds the sample values of expression data to the output files."""
def build_expression(row, samples):
    exprrows=[]
    for s in samples:
        newrow=[s,]
	newrow.append(row[int(colnames['ID_REF'])])
	newrow.append(row[int(colnames[s])])
	exprrows.append("\t".join(newrow))
    return "\n".join(exprrows)+"\n"
"""
initialise a counter to count how many probe rows were processed.
           writes the data to the files.
also has an exception to help identify bugs with the code.
"""
rows=0
for line in fh.readlines():
    try:
        if line[0]=='!':
            continue
        row=line.strip().split('\t')
        genefile.write(buildrow(row, genefields))
        probefile.write(buildrow(row,probefields))
        expressionfile.write(build_expression(row, samples))
        rows=rows+1
    except:
		pass
#Closes the output files. 
genefile.close()
probefile.close()
expressionfile.close()
""" print message informing that user of the progress and evident success of the script.""" 
print '%s rows processed'%rows





