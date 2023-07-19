#!/bin/bash

#David Rauch

#do MetaRNN LDLIBRARY thing
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/storage/chen/home/u250677/miniconda3/envs/MetaRNN/lib

#naviage to raw data dir
#cd /storage/chentemp/derauch/models/results/patient_output
cd /storage/chentemp/derauch/models/results/patient_reformatted

#remove old outputs
rm *
printf "removed old files\n"

#create the vcf files
sh /storage/chentemp/derauch/code/wrappers/makevcf/makevcf.sh

printf "\ndata formatted\n\n"

output="/storage/chentemp/derauch/models/results/MetaRNN/patient_output"

for input in *.vcf
do
	
	cd /storage/chentemp/derauch/models/MetaRNN

	printf "\n MetaRNN: Running $input \n"

	python /storage/chentemp/derauch/models/MetaRNN/MetaRNN.py hg19 /storage/chentemp/derauch/models/results/patient_reformatted/$input

done
