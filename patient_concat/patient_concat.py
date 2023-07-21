#!/usr/bin/env python3

import glob
import pandas as pd
import os

os.chdir("/storage/chentemp/derauch/data/inframe_indel/patient_data/patient_output/")

files = glob.glob("*.avinput")

first = files.pop(0)

origin_df = pd.read_csv(first, sep="\t")
print(f"looking at: {first}")

origin_df = origin_df.rename(columns={"Start":"Position"})

origin_df["Patient_ID"] = origin_df["Patient_ID"].astype(object)

#print(origin_df.columns)

origin_df = origin_df.drop("End", axis=1)

columns = origin_df.columns.tolist()

for file in files:
	this_df = pd.read_csv(file, sep="\t")
	print(f"working on {file}")

	#reformat this_df to make it like the rest
	this_df = this_df.rename(columns={"Start":"Position"})
	this_df.drop("End", axis=1, inplace=True)

	this_df["Patient_ID"] = this_df["Patient_ID"].astype(object)

	master_df = pd.merge(origin_df, this_df, on=columns, how="outer")

	origin_df = master_df

#save the df as csv
master_df.to_csv("/storage/chentemp/derauch/data/inframe_indel/patient_data/merged_patient_rawdata.tsv", index=False, sep="\t")

