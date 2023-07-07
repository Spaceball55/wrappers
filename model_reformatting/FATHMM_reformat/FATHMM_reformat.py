#!/usr/bin/env python

#David Rauch
#Baylor College of Medicine MHG
#07/05/2023

###

#strips the REF and ALT columns of their first nucleotide from model outputs to standardize them
#usage:
# python FATHMM_reformat.py [file.tsv]

#inputs:
# file.tsv -> some .tsv file (usually either CADD output or MetaRNN)

import sys
import pandas as pd

# read the file that you want to edit
file = sys.argv[1]

print(file)

print(f"Working on: {file}")
df = pd.read_csv(file, sep='\t')

df_renamed = df.rename(columns={"Chr":"#CHROM", "Wildtype":"REF", "Mutant":"ALT"})

#strip "REF" column
df_renamed["REF"] = df_renamed["REF"].str[1:]

df_renamed["ALT"] = df_renamed["ALT"].str[1:]

#rename so we don't overwrite original data
new_name =  "edited_" + file

print(f"Saving {new_name}")

# save new file as another .tsv file
df_renamed.to_csv(new_name, index=False, sep='\t')
