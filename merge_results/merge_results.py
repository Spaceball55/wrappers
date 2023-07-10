#!/usr/bin/env python

# get_scores
# David Rauch
# BCM MHG
# 7/6/2023

### 

import pandas as pd
import glob
import sys
import os

## get files
#file1 = sys.argv[1]
#file2 = sys.argv[2]
#df1 = pd.read_csv(file1, sep="\t")
#df2 = pd.read_csv(file2, sep="\t")
#print(f"working with {file1} and {file2}")
#
#master_df = pd.merge(df1, df2, on=["#CHROM", "Position", "REF", "ALT"], how="outer")
#
#newfile_name = "merged_test.tsv"
#
#master_df.to_csv(newfile_name, index=False, sep="\t")
#
####################

tsv_files = glob.glob('*.tsv')

#for debugging
print(tsv_files)

#TARGETS = ['VEST score (inframe indels)', 'Prediction', 'RawScore', 'PHRED', 'MetaRNN-indel_score', 'FATHMM-indel Score', 'predicted class']

first = tsv_files.pop(0)

print(f"first file is {first}")

origin_df = pd.read_csv(first, sep="\t")

for file in tsv_files:
	#read the tsv file
	print(f"Reading the file {file}\n")

	#get an individual df
	this_df = pd.read_csv(file, sep="\t")

	this_df["#CHROM"] = this_df["#CHROM"].astype(object)

	print(this_df.dtypes)

	#create a master df that merges the original df and another df
	master_df = pd.merge(origin_df, this_df, on=["#CHROM", "Position", "REF", "ALT"], how="outer")

	#make the new original df the merge of all the previous dfs
	origin_df = master_df

# get current working directory
WORKING_DIR = os.getcwd()

newfile_name = "results/merged_results.tsv"

if not os.path.isdir("results"):
	path = os.path.join(WORKING_DIR, "results")
	os.makedirs(path)
	print(f"created a directory in {path}")

master_df.to_csv(newfile_name, index=False, sep="\t")

#	#old method
#	#previous_dfs = pd.concat([master_df, this_df], join='outer')
#	#master_df = previous_dfs
#	
#	#using merge instead
#	#merge based on the important characteristics of our variant: #CHROM, Pos, REF, and ALT
#	master_df.merge(this_df, on=['#CHROM', 'Position', 'REF', 'ALT'])

#master_df.to_csv('output.csv', index=False, index_label=False)



