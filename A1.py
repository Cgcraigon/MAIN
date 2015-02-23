#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
Class Protein();
protein_id=''
protein_sequence=''

def__init__(self,id,sequence)
   self.protein_id=id
   self.protein_sequence=sequence
myprot=Protein('A1','blahblah')

myprot=

def aminocount(self,aminoacid):
    aacount=0
for a in self.protein_sequence
if a==aminoacid 
  aacount = aacount+1
  return aacount 

expsql='SELECT expression from expression where sample_ID=%s and probe_id in %s'
db=DBhandler()
cursor=db.cursor()
cursor.execute(expsql,(self.gene_id,)self.probe_id)
