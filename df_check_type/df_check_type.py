#/usr/bin/env python

#David Rauch
#Baylor College of Medicine MHG
#07/06/2023

###

#Usage:
# python df_check_type [file]
# inputs:
# file -> a .tsv file 

#outputs:
# the datatype of each column in the dataframe

import pandas as pd
import sys

file = sys.argv[1]

df = pd.read_csv(file, sep="\t")

print(df.dtypes)
