#!/usr/bin/env python

#David Rauch
#Baylor College of Medicine MHG
#7/21/2023

##

#filters out the raw patient data for only indels

import pandas as pd

df = pd.read_csv('/storage/chentemp/derauch/data/inframe_indel/patient_data/merged_patient_rawdata.tsv', sep="\t")

filtered_df = df[abs(df['Ref'].str.len() - df['Alt'].str.len()) > 0]

filtered_df.to_csv('/storage/chentemp/derauch/data/inframe_indel/patient_data/patient_indels_raw.tsv', index=False, sep="\t")
