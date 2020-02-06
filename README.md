# 2019-nCoV Protein Sequences

In this repo I collected various files that may be useful for the community / those interested in the 2019-nCoV, aka. the novel CoronaVirus (also known as Wuhan coronavirus, or Wuhan seafood market pneumonia virus). If you have any questions contact me on TW: [@sacdallago](https://twitter.com/sacdallago)


### Files:

1. All protein products translated from sequenced genomes on NCBI ([from NCBI protein](https://www.ncbi.nlm.nih.gov/protein/?term=txid2697049[Organism:noexp])) as a single FASTA file. This resource is updated regularly: [files/nCoV.fasta](files/nCoV.fasta)

1. The spike/surface glycoprotein translated from the first (Dec 19) sequenced genome of the virus (https://www.ncbi.nlm.nih.gov/protein/1791269090): [files/nCoV_2019_glycoprotein.fasta](files/nCoV_2019_glycoprotein.fasta)

1. All protein products from SARS ([from NCBI protein](https://www.ncbi.nlm.nih.gov/protein/?term=txid694009[Organism:noexp]])) and MERS ([from NCBI protein](https://www.ncbi.nlm.nih.gov/protein/?term=txid1335626[Organism:noexp])):
    - [files/SARS.fasta](files/SARS.fasta)
    - [files/MERS.fasta](files/MERS.fasta)

1. All protein products that match "spike glycoprotein" on NCBI ([from NCBI protein](https://www.ncbi.nlm.nih.gov/protein/?term=spike+glycoprotein)): [files/spike_glycoproteins.fasta](files/spike_glycoproteins.fasta)

1. Spike glycoproteins reduced to 90% similarity via CD-HIT: [files/cd-hit/spike_glycoproteins_90.fasta](files/cd-hit/spike_glycoproteins_90.fasta)

1. Multiple alignments (via `jackhmmer` and `evcouplings`) of the dec 2019 nCoV sequenced spike glycoprotein (see above) against all spike glycoproteins found on NCBI (see above): [maintenance.dallago.us/public/ncov/alignments](http://maintenance.dallago.us/public/ncov/alignments).










### Data & tools:

- RAW data from NCBI
- Scripts to download data from NCBI in this repository
- `jackhmmer` was used to produce alignments
- `evcouplings` via the evcouplings.org server and the evcouplings python pipeline
- `cd-hit`
