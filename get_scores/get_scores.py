# get_scores
# David Rauch
# BCM MHG
# 7/3/2023

### 

import pandas as pd

tsv_files = glob.glob('*.tsv')

dfs = []

for file in tsv_files:
	#read the tsv file
	df = pd.read_csv(file, sep="\t")

	dfs.append(df)

master_df = pd.concat(dfs)

