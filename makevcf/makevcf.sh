#!/bin/sh

#David Rauch
#Baylor College of Medicine MHG
#7/17/2023

# makevcf.sh
# a script that takes all of the .avinput files in a dir and turns them into .vcf files for MetaRNN (or other model) analysis

#inputs:
# main (dir): the directory containing all of the input files to turn into a .vcf file

#outputs:
# the files turned into .vcf format

##################

#full database
cd /storage/chentemp/mwang/Mutscore_missense/patient_output/

main="/storage/chentemp/derauch/models/results/patient_reformatted"

for input in *.avinput
do

printf "\n**************\n$input\n"

cd /storage/chentemp/mwang/Mutscore_missense/patient_output/

##extract columns chr/pos/ref/alt
less $input | awk '{ print $1"\t"$2"\t.\t"$4"\t"$5"\t60\tPASS\t.\tGT:VR:RR:DP:GQ\t0/1:100:100:200:."}' > ${main}/vcf_format

##add VCF header
cat /storage/chentemp/mwang/inframe_indel/vcf_header ${main}/vcf_format > ${main}/${input}.vcf

##change chromosome notations. e.g. 1 -> chr1.
#awk '{if($0 !~ /^#/) print "chr"$0; else print $0}' ${main}/${input}.vcf > ${main}/${input}.with_chr.vcf

rm ${main}/vcf_format 
done

printf "\nfinished\n"
