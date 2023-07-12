#!/usr/bin/env python

# David Rauch
# BCM MHG
# 7/6/2023

### 

# merge_results.py 

# takes a model's reformatted output (detailed below) and puts them all into one dataframe

#Arguments:
# None
#Outputs:
# a merged .tsv file of all of the results from different pathogenicity prediction models

#NOTE: this script was written for Inframe-Indel models - it should work for other kinds of models, but be sure to check that the outputs have the required columns!

# usage:
# ./merge_results.py

#NOTES ABOUT INPUTS:
# Each of the outputs from the models need to be slightly reformatted. They all need to have matching "#CHROM". "Position", "REF", and "ALT" headers (case-sensitive) - I have written python scripts to reformat 
# CADD, MetaRNN, FATHMM-Indel, Mutation_Taster_2021, and VEST4 outputs. Other models will likely need custom scripts. 
# You need to be sure that the column indicated chromosomes is titled "#CHROM", and so forth.

# Also, note the datatypes when merging the files - there might be differences between the model outputs, and those will need to be resolved in their own respective reformatting scripts. 

import pandas as pd
import glob
import sys
import os

tsv_files = glob.glob('*.tsv')

#for debugging
print(tsv_files)

# pop off one dataframe to create the first df so we can merge others into it
first = tsv_files.pop(0)

print(f"first file is {first}")

origin_df = pd.read_csv(first, sep="\t")

for file in tsv_files:
	#read the tsv file
	print(f"Reading the file {file}\n")

	#get an individual df
	this_df = pd.read_csv(file, sep="\t")

	this_df["#CHROM"] = this_df["#CHROM"].astype(object)

	# if there are issues merging because of different datatypes, uncomment below and investigate the datatypes of all of your model outputs
	#print(this_df.dtypes)

	#create a master df that merges the original df and another df on specific columns
	master_df = pd.merge(origin_df, this_df, on=["#CHROM", "Position", "REF", "ALT"], how="outer")

	#make the new original df the merge of all the previous dfs
	origin_df = master_df

# get current working directory
WORKING_DIR = os.getcwd()

newfile_name = "results/merged_results.tsv"

# save the merged outputs
if not os.path.isdir("results"):
	path = os.path.join(WORKING_DIR, "results")
	os.makedirs(path)
	print(f"created a directory in {path}")

master_df.to_csv(newfile_name, index=False, sep="\t")

