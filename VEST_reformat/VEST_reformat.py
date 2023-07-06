#!/usr/bin/env python

#David Rauch
#BCM MHG
#7/6/2023

## 

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


