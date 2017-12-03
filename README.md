The scripts contained within this repository can be used to perform some basic metagenomics analysis.

FASTAQ Stats

This script counts the number of sequences and residues contained within a FASTA or FASTQ file. It accepts files with the extensions .fasta, .fa, .fastq or .fq. 

Fragment Recruitment Plot

This script creates fragment recruitment plots using SAM files. The script assumes that the input SAM files contain an MD field. The MD field is optional in SAM files, but it may be added with the samtools command:
samtools fillmd -S file.sam genomic.fna > file.md.sam

Shorten MGM Output

This script shortens the output .lst file from MetaGeneMark analysis to include only the sequence information where genes have been predicted. The script assumes that version v.3.38 of MetaGeneMark was used with the -b argument.
