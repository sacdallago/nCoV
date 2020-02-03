#!/bin/python

import argparse

from Bio import Entrez

parser = argparse.ArgumentParser(description='Searches for protein sequences in the Title Word field ([TITL]) based on any provided key terms.\nSee here for further details: http://cbsu.tc.cornell.edu/resources/seq_comp/pb607_introductory/entrez/ncbi_entrez.html')
parser.add_argument('-e', action='store', dest='EmailAddress', required=True, help='Entrez requires your email address.')
parser.add_argument('-t', action='store', dest='SearchTerm', required=True, help='Requires a search term (wrap in double quotes).')

arguments = parser.parse_args()

Entrez.email = arguments.EmailAddress

handle = Entrez.esearch(db='protein', term=arguments.SearchTerm, retmax=100000)
results = Entrez.read(handle)
handle.close()

with open(arguments.SearchTerm + '.fasta', "w") as fasta_file:
  for gi in results['IdList']:
    handle = Entrez.efetch(db='protein', id=gi, rettype='fasta')
    print(handle.read(), file=fasta_file)
    handle.close()

