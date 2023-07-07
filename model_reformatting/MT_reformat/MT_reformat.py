#!/bin/bash/env python

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

file = sys.argv[1]

print(f"Working on {file}")

df = pd.read_csv(file, sep="\t")

renamed_col = df.rename(columns={"Chr":"#CHROM", "Ref":"REF", "Alt":"ALT"})

#get rid of weird last line
renamed_col.drop(renamed_col[renamed_col["#CHROM"] == "############## MutationTaster predictions were generated using data from Ensembl 102 ##############"].index, inplace=True)

#fix type mismatch issues
renamed_col["#CHROM"] = renamed_col["#CHROM"].astype(pd.Int64Dtype())

renamed_col["Position"] = renamed_col["Position"].astype(pd.Int64Dtype())

new_name = "edited_" + file

renamed_col.to_csv(new_name, index=False, sep="\t")
