#!/usr/bin/env python

import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import re

def main():	
	#check for sam file
	for fn in sys.argv[1:]:
		if fn.endswith('.sam'):
			open_file = open(fn, 'r')
			position, identity = get_matches(open_file)
			fragplot(position, identity)
		else:
			print "Script requires SAM file as first argument"
			sys.exit(1)

def get_matches(open_file):
	#estabish list to hold read info, matches, mismatches
	columns = []
	match_list = []
	mismatch_list =[]
	positions = []
	identity_list = []
	m = 0
	#find matches and mismatches in cigar, M columns
	for line in open_file:
		if not line.startswith('@'):
			columns = line.rstrip().split()
			#find M value in cigar
			cigar = columns[5]
			matches = re.search(r'[0-9]+M', cigar)
			#remove M from matches found
			if matches:
				matches = matches.group()
				matches = matches.replace('M', '')
				match_list.append(float(matches))
				#get genome position for reads with matches
				positions.append(int(columns[3]))
				#print "matches: "+ str(matches)
			#search for MD field
			for column in columns:
				if column.startswith('MD'):
					#count mismatches as indicated by basepairs in MD string
					mismatch = len(re.findall(r'[ACTG]', column))
					mismatch_list.append(float(mismatch))
					#print "mismatches: " + str(mismatches)
		
	for match in match_list:
		total = match_list[m]+mismatch_list[m]
		identity = 100*(match_list[m]/(total))
		identity_list.append(identity)
		m += 1
	
	return positions, identity_list


def fragplot(position, identity):
	plt.scatter(position, identity)
	x_max = max(position) + (max(position)*0.05)
	y_min = min(identity) - 0.1
	y_max = max(identity) + 0.1
	plt.axis([0, x_max, y_min, y_max])
	plt.title("Fragment Recruitment Plot")
	plt.xlabel("Genomic Position")
	plt.ylabel("Percent Identity")
	plt.show()


if __name__ == '__main__':
    main()
