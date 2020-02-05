#!/bin/python

import argparse
import xml.etree.ElementTree as ET
from pandas import DataFrame
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

handle = Entrez.efetch(db='protein', id=results['IdList'], rettype='gp', retmode='xml')
tree = ET.fromstring(handle.read())
handle.close()

proteins = []

for child in tree:
    protein = {
        'locus': child.find('GBSeq_locus').text,
        'primary_accession': child.find('GBSeq_primary-accession').text,
        'accession_version': child.find('GBSeq_accession-version').text,
    }

    for qualifier in child.findall('.//GBQualifier'):
        if qualifier.find('GBQualifier_name').text == 'isolate':
            protein['isolate'] = qualifier.find('GBQualifier_value').text

    proteins.append(protein)

df = DataFrame(proteins)
df.to_csv((arguments.FileName if arguments.FileName else 'sequences') + '.txt',
          sep='\t',
          index=False)

