#!/usr/bin/env python

#David Rauch
#Baylor College of Medicine MHG
#07/05/2023

###

#strips the REF and ALT columns of their first nucleotide from model outputs to standardize them
#usage:
# python df.rmchar.py [file.tsv]

#inputs:
# file.tsv -> some .tsv file (usually either CADD output or MetaRNN)

import sys
import pandas as pd

# read the file that you want to edit
files = sys.argv[1:]

print(files)

for file in files:
	print(f"Working on: {file}")
	df = pd.read_csv(file, sep='\t')

	#strip "REF" column
	df["REF"] = df["REF"].str[1:]

	df["ALT"] = df["ALT"].str[1:]

	df["Position"] = df["Position"].astype(pd.Int64Dtype())

	#rename so we don't overwrite original data

	new_name = "edited_" + file

	print(f"Saving {new_name}")

	# save new file as another .tsv file
	df.to_csv(new_name, index=False, sep='\t')

print('Done!')
