# 2019-nCoV Protein Sequences

In this repo I collected various files that may be useful for the community / those interested in the 2019-nCoV, aka. the novel CoronaVirus (also known as Wuhan coronavirus, or Wuhan seafood market pneumonia virus). If you have any questions contact me on TW: [@sacdallago](https://twitter.com/sacdallago)


### Files:

1. All protein products translated from sequenced genomes on NCBI ([from NCBI protein](https://www.ncbi.nlm.nih.gov/protein/?term=txid2697049[Organism:noexp])) as a single FASTA file. This resource is updated regularly: [files/nCoV.fasta](files/nCoV.fasta)

2. The spike/surface glycoprotein translated from the first (Dec 19) sequenced genome of the virus (https://www.ncbi.nlm.nih.gov/protein/1791269090): [files/nCoV_2019_glycoprotein.fasta](files/nCoV_2019_glycoprotein.fasta)

3. All protein products from SARS ([from NCBI protein](https://www.ncbi.nlm.nih.gov/protein/?term=txid694009[Organism:noexp]])) and MERS ([from NCBI protein](https://www.ncbi.nlm.nih.gov/protein/?term=txid1335626[Organism:noexp])):
    - [files/SARS.fasta](files/SARS.fasta)
    - [files/MERS.fasta](files/MERS.fasta)

4. All protein products that match "spike glycoprotein" on NCBI ([from NCBI protein](https://www.ncbi.nlm.nih.gov/protein/?term=spike+glycoprotein)): [files/spike_glycoproteins.fasta](files/spike_glycoproteins.fasta)

5. The alignment (`jackhmmer -T 0.2 --domT 0.2 --incT 0.2 --incdomT 0.2`) of the dec 2019 nCoV sequenced spike glycoprotein (see above) against all spike glycoproteins found on NCBI (see above):
     - STOCKHOLM format: [maintenance.dallago.us/public/ncov/alignment.sto](http://maintenance.dallago.us/public/ncov/alignment.sto)
     - A2M format: [maintenance.dallago.us/public/ncov/alignment.a2m](http://maintenance.dallago.us/public/ncov/alignment.a2m)










### Data & tools:

- RAW data from NCBI
- Scripts to download data from NCBI in this repository
- `jackhmmer` was used to produce alignments