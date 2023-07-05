#David Rauch
#Baylor College of Medicine MHG
#07/05/2023

###

import sys
import pandas as pd

files = sys.argv[1:]

print('Hello world!')

for file in files:
	print(file)
	df = pd.read_csv(file, sep='\t')

	df["REF"].str[1:]

	df["ALT"].str[1:]
	
	print(f"Saving {file}\n")
	
	df.to_csv(file, index=False, sep='\t')

