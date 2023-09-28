#!/usr/bin/env python

#David Rauch
#Baylor College of Medicine MHG
#07/06/2023

##

#reformats MutationTaster Indel output files to fit them all in a chart

#usage
# python MT_reformat.py [file.tsv]
#inputs
# file.tsv -> a .tsv file that's the output of mutationtaster

import pandas as pd
import sys
import os

file = sys.argv[1]

print(f"Working on {file}")

df = pd.read_csv(file, sep="\t")

renamed_col = df.rename(columns={"Chr":"#CHROM", "Ref":"REF", "Alt":"ALT", "Prediction": "Mutation_Taster_Prediction"})

#get rid of weird last line
renamed_col.drop(renamed_col[renamed_col["#CHROM"] == "############## MutationTaster predictions were generated using data from Ensembl 102 ##############"].index, inplace=True)

#fix type mismatch issues
#renamed_col["#CHROM"] = renamed_col["#CHROM"].astype(pd.Int64Dtype())
#renamed_col["#CHROM"] = renamed_col["#CHROM"].astype(object)
renamed_col['#CHROM'] = renamed_col['#CHROM'].apply(lambda x: str(x))

renamed_col["Position"] = renamed_col["Position"].astype(pd.Int64Dtype())

# make the position 0-based deprecated, no longer necessary
#renamed_col["Position"] = renamed_col["Position"] - 1

# change the 23rd chromosome to chromosome X
renamed_col["#CHROM"] = renamed_col["#CHROM"].replace("23", "X")

# save into the results directory
DIR = "reformatted_outputs"
try:
	os.chdir(DIR)
except:
	#if the results directory doesn't exist, make it
	print('Creating reformatted_outputs/')
	os.mkdir(DIR)
	os.chdir(DIR)

new_name = "edited_" + file


#print(renamed_col.dtypes)

renamed_col.to_csv(new_name, index=False, sep="\t")
