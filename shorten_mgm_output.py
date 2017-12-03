#!/usr/bin/env python

import sys

def main():
	#check for .lst as first argument
	try:
		fn =  sys.argv[1]
		if fn.endswith('.lst'):
			open_file = open(fn, 'rU')
			parse_lst(open_file)
	except IndexError:
		print "No file found."
		sys.exit(1)

def parse_lst(open_file):
  #ignore header
	x = -7
	for line in open_file:
		#.rstrip removes whitespace from end of string
		line = line.rstrip()
		#get found genes
		if line.startswith("FASTA"):
			x = 1
			definition = line
		else:
			x += 1
			#output found genes into file
			if x == 5:
				gene_info = line
			if x == 8:
				with open("short.lst", "a") as short_lst:
					short_lst.write("%s\n%s\n" % (definition, gene_info))

if __name__ == '__main__':
    main()
