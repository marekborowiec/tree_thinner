#! /usr/bin/env python
# tree_thinner.py by Marek Borowiec


from __future__ import division
import sys, re

Usage = """
Given burnin and trees_number this program extracts 
the desired number of trees from the posterior 
and prints output that can be redirected to a file.
Usage:
	tree_thinner.py your_sample_file.runX.t burnin trees_number > new_file.txt
Example:
	tree_thinner.py my_ants_20m.run1.t 5000 1000 > thinned_my_ants.run1.txt
"""
# check if there are enough arguments passed
if len(sys.argv) < 4:
	print(Usage)

else:
	# define file name, burnin, and number of trees to be retained from sys.argv
	FileName = sys.argv[1]
	Burnin = sys.argv[2]
	Trees_no = sys.argv[3]

	# this string appears in MrBayes NEXUS tree files and signifies a tree from the posterior
	Tree_string = str("tree gen")
	
	# define search pattern to find the NEXUS block, i.e., all lines that are not trees and not the end statements
	Block_search = re.compile("^(?!.*tree gen*|.*end*).*")

	# get all lines from the file
	All_lines_list = [line.split(';') for line in open(FileName)]
	
	# find lines to be printed as the NEXUS block
	Block = [x for i, x in enumerate(All_lines_list) if re.search(Block_search, str(x))]
	
	# find all tree lines
	All_trees_list = [x for i, x in enumerate(All_lines_list) if re.search(Tree_string, str(x))]
	
	# calculate at what interval the trees shuld be sampled from post-burnin 
	Iteration = ( len(All_trees_list) - int(Burnin) - 1 ) / int(Trees_no)
	
	# get only post-burnin trees (add one to account for the starting tree)
	No_burnin_trees = All_trees_list[(int(Burnin) + 1):]

	# get the thinned sample of post-burnin trees 
	Thinned_trees = No_burnin_trees[0::int(Iteration)]

	# print the block, thinned sample, and end statement
	print str('\n'.join(map(str, Block))).replace("['", "").replace("\\n']", "").replace("', '", ";")
	print str('\n'.join(map(str, Thinned_trees))).replace("['", "").replace("\\n']", "").replace("', '", ";")
	print "end;"

