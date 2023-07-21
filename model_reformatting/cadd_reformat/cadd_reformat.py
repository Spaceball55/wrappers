#!/usr/bin/env python

#David Rauch
#Baylor College of Medicine MHG
#07/05/2023

###

#strips the REF and ALT columns of their first nucleotide from model outputs to standardize them
#usage:
# python cadd_reformat.py [file.tsv]

#inputs:
# file.tsv -> the .tsv output file from CADD

import sys
import pandas as pd
import os

# read the file that you want to edit
file = sys.argv[1]

print(f"Working on: {file}")
df = pd.read_csv(file, sep='\t')


#strip "REF" column
df["Ref"] = df["Ref"].str[1:]

df["Alt"] = df["Alt"].str[1:]

renamed_df = df.rename(columns={"#Chrom":"#CHROM","Pos":"Position", "Ref":"REF", "Alt":"ALT", "RawScore": "CADD_Raw"})

# save into the results directory
DIR = "reformatted_outputs"
try:
	os.chdir(DIR)
except:
	#if the results directory doesn't exist, make it
	print('Creating reformatted_outputs')
	os.mkdir(DIR)
	os.chdir(DIR)

#rename so we don't overwrite original data
new_name =  "edited_" + file

print(f"Saving {new_name}")

# save new file as another .tsv file
renamed_df.to_csv(new_name, index=False, sep='\t')
