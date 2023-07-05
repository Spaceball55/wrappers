# get_scores
# David Rauch
# BCM MHG
# 7/3/2023

### 

import pandas as pd
import glob

tsv_files = glob.glob('*.tsv')

#TARGETS = ['VEST score (inframe indels)', 'Prediction', 'RawScore', 'PHRED', 'MetaRNN-indel_score', 'FATHMM-indel Score', 'predicted class']

master_df = pd.DataFrame()

for file in tsv_files:
	#read the tsv file
	print(f"Reading the file {file}\n")
	this_df = pd.read_csv(file, sep="\t")
	
	#old method
	#previous_dfs = pd.concat([master_df, this_df], join='outer')
	#master_df = previous_dfs
	
	#using merge instead
	#merge based on the important characteristics of our variant: #CHROM, Pos, REF, and ALT
	master_df.merge(this_df, on=['#CHROM', 'Position', 'REF', 'ALT'])


master_df.to_csv('output.csv', index=False, index_label=False)



