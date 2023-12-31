#!/bin/sh

input="/storage/chentemp/derauch/data/inframe_indel/meta_indel/indel_eval.vcf"
#output="tool_test_dataset"
output="/storage/chentemp/derauch/data/inframe_indel/meta_indel/indel_eval"

#cd /storage/chentemp/mwang/inframe_indel/

##select first 200 variant for test run
#head -n 201 ${input} > tmp

##extract columns chr/pos/ref/alt
#cannon dataset
tail -n+2 $input | awk '{ print $1"\t"$4"\t.\t"$6"\t"$7"\t60\tPASS\t.\tGT:VR:RR:DP:GQ\t0/1:100:100:200:."}' > vcf_format

##add VCF header
cat /storage/chentemp/derauch/code/wrappers/VCF_format/vcf_header vcf_format > ${output}.vcf

##change chromosome notations. e.g. 1 -> chr1.
awk '{if($0 !~ /^#/) print "chr"$0; else print $0}' ${output}.vcf > ${output}.with_chr.vcf

rm  vcf_format
