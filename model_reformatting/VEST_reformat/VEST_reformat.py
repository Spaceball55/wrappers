#!/usr/bin/env python

#David Rauch
#BCM MHG
#7/6/2023

##

#Reformats VEST4 outputs from CRAVAT to standardize them among other models for ease of merging them together

#usage
# python VEST_reformat.py [file.tsv]
#inputs:
# file.tsv -> a .tsv file that is outputted from VEST analysis
#outputs:
# an edited .tsv file that is standardized with the others 

import pandas as pd
import sys
import re

#get the first argument passed after calling this script
inputfile = sys.argv[1]

vest0 = pd.read_csv(inputfile, sep="\t")

vest0["Reference base(s)"] = vest0["Reference base(s)"].str.replace("-", "")

vest0['Alternate base(s)'] = vest0['Alternate base(s)'].str.replace('-', "")

vest0["Chromosome"] = vest0["Chromosome"].str[3:]

#rename the columns to keep VEST4 output consistent with the rest
renamed = vest0.rename(columns={"Reference base(s)": "REF", "Alternate base(s)":"ALT", "Chromosome":"#CHROM"})

new_name = "edited_" + inputfile

renamed.to_csv(new_name, index=False, sep="\t")
