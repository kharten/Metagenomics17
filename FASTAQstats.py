#!/usr/bin/env python

import sys
import gzip

def main():
	#create tuples for different file types
	fasta_tup = ('.fa', '.fasta')
	fastq_tup = ('.fq', '.fastq')

	#check for fasta or fastq as first argument
	try:
		fn =  sys.argv[1]
		if fn.endswith('.gz'):
			open_file = gzip.open(fn, 'rb')
			#read_file = open_file.readlines()
			parse_fasta(open_file)
		elif fn.endswith(fasta_tup):
			open_file = open(fn, 'rU')
			parse_fasta(open_file)
		elif fn.endswith(fastq_tup):
			open_file = open(fn, 'rU')
			parse_fastq(open_file)

	except IndexError:
		print "No file found."
		sys.exit(1)


def parse_fasta(open_file):

	seq_desc = 0	
	seqs = 0	

	#assign fasta descriptions to list (seq_desc), and descriptions, seqs to dictionary (store_fasta)
	for line in open_file:

		#.rstrip removes whitespace from end of string
		line = line.rstrip()

		if line.startswith(">"):
			seq_desc += 1
		else:
			seqs += len(line)

	print "Total sequences found: %s" % seq_desc
	print "Total residues found: %s" % seqs


def parse_fastq(open_file):

	seq_desc = 0
	seqs = 0
	
	#variable to track lines in fastq entry
	x = 4
	
	#assign fastq descriptions to list (seq_desc), and descriptions, seqs to dictionary (store_fastq)
	for line in open_file:
		line = line.rstrip()
		if x == 4 and line.startswith("@"):
			seq_desc += 1
			x = 1
		else:
			if x == 1:
				seqs += (len(line))
			x += 1

	print "Total sequences found: %s" % seq_desc
	print "Total residues found: %s" % seqs


if __name__ == '__main__':
    main()
