#!/bin/sh

#full database
cd /storage/chentemp/mwang/Mutscore_missense/patient_output/

#small testcase of n=2 patients
#cd /storage/chentemp/derauch/data/inframe_indel/patient_test

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

##run metaRNN

#cd $main
#printf "\nMetaRNN: running $main/$input.vcf \n"

#python /storage/chentemp/derauch/models/MetaRNN/MetaRNN.py hg19 $main/$input.vcf

rm ${main}/vcf_format 
done

printf "\nfinished\n"
