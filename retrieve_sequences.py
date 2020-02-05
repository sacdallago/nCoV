#!/bin/python

import argparse
from Bio import Entrez

parser = argparse.ArgumentParser(description='Searches for protein sequences in the Title Word field ([TITL]) based on any provided key terms.\nSee here for further details: http://cbsu.tc.cornell.edu/resources/seq_comp/pb607_introductory/entrez/ncbi_entrez.html')
parser.add_argument('-e', action='store', dest='EmailAddress', required=True, help='Entrez requires your email address.')
parser.add_argument('-t', action='store', dest='SearchTerm', required=True, help='Requires a search term (wrap in double quotes).')
parser.add_argument('-o', action='store', dest='FileName', required=False, help='Output file name (e.g.: sequences).')

arguments = parser.parse_args()

Entrez.email = arguments.EmailAddress

handle = Entrez.esearch(db='protein', term=arguments.SearchTerm, retmax=100000)
results = Entrez.read(handle)
handle.close()

with open((arguments.FileName if arguments.FileName else 'sequences') + '.fasta', "w") as fasta_file:
    handle = Entrez.efetch(db='protein', id=results['IdList'], rettype='fasta')
    print(handle.read(), file=fasta_file)
    handle.close()
