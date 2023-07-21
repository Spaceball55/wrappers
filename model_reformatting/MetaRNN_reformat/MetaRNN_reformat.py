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
import re
import os

# read the file that you want to edit
file = sys.argv[1]

print(file)

print(f"Working on: {file}")
df = pd.read_csv(file, sep='\t')

#strip "REF" column
df["REF"] = df["REF"].str[1:]

df["ALT"] = df["ALT"].str[1:]

df.rename(columns={"POS":"Position", "MetaRNN-indel_score": "MetaRNN-Indel"}, inplace=True)

# save into the results directory
DIR = "reformatted_outputs"
try:
	os.chdir(DIR)
except:
	#if the results directory doesn't exist, make it
	print('Creating reformatted_outputs/')
	os.mkdir(DIR)
	os.chdir(DIR)

#rename so we don't overwrite original data
new_name =  "edited_" + file

print(f"Saving {new_name}")

# save new file as another .tsv file
df.to_csv(new_name, index=False, sep='\t')
