#!/bin/bash

#David Rauch
#Baylor College of Medicine MHG
#7/21/2023

###

#Parses patient output and gets their #CHROM, POS, REF, ALT, and allele counts

patient_data_folder="/storage/chentemp/mwang/Mutscore_missense/patient_output/"
output="/storage/chentemp/derauch/data/inframe_indel/patient_data/patient_output"

#header="Chr	Start	End	Ref	Alt	Patient_ID	Geno	Genotype	alt_reads	ref_reads	total_reads	gnomad_WES_AC	gnomad_WGS_AC	gnomad_WES_AF	gnomad_WGS_AF	gnomad_WES_AN	gnomad_WGS_AN"

patient_files=$(ls $patient_data_folder | grep ".avinput")

cd $patient_data_folder

for patient in $patient_files
do
	printf "working on $patient \n"
	cat /storage/chentemp/derauch/code/wrappers/patient_parser/patient_header $patient > ${output}/${patient}
	printf "saved to ${output}.${patient} \n"
done
