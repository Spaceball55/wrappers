#!/usr/bin/env python

#David Rauch
#Baylor College of Medicine MHG
#7/19/2023

"""
merge_MetaRNN.py

a script that merges the outputs of MetaRNN in one giant dataframe, with the columns aligned

inputs:
Files with the suffix .indel.annotated

**Run inside of the directory that has the files you wish to merge together

outputs:
master_df.tsv (Pandas dataframe): a giant master dataframe of all of the output files concatenated
"""

import pandas as pd
import os
import sys
import glob

os.chdir("/storage/chentemp/derauch/models/results/indel_patients/")

#get every annotation
files = glob.glob("*.indel.annotated*")

#pop off the first annotation and use it to start the master df
first = files.pop(0)

master_df = pd.read_csv(first, sep="\t")

for file in files:
	#read the file
	this_df = pd.read_csv(file, sep="\t")

	#concat master_df and this_df
	master_df = pd.concat([master_df, this_df])

#save to a dir to find later
master_df.to_csv("/storage/chentemp/derauch/models/results/MetaRNN_patients_merged/patient_indels_merged.tsv", sep="\t", index=False)
