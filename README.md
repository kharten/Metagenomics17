The scripts contained within this repository can be used to perform some basic metagenomics analysis.

FASTAQstats

This script counts the number of sequences and residues contained within a FASTA or FASTQ file. It accepts files with the extensions .fasta, .fa, .fastq or .fq. 

FragmentRecruitmentPlot

This script creates fragment recruitment plots using SAM files. The script assumes that the input SAM files contain an MD field. The MD field is optional in SAM files, but it may be added with the samtools command:
samtools fillmd -S file.sam genomic.fna > file.md.sam
