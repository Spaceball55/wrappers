#!/bin/sh

#created VCF file for FATHMM-indel
#modified from Meng Wang
#David Rauch
#BCM MHGCP
#6/21/2023

input="/storage/chentemp/derauch/data/inframe_indel/meta_indel/indel_eval.tsv"
output="/storage/chentemp/derauch/data/inframe_indel/meta_indel/indel_eval"

##select first 200 variant for test run
#head -n 201 ${input} > tmp

##extract columns chr/pos/ref/alt
# tail -n+2 tmp  |  awk '{ print $1"\t"$4"\t"$6"\t"$7"\t60"}' > vcf_format

# for when we do not have a headless VCF (commented out when headless)
#tail -n+2 $input  |  awk '{ print $1"\t"$4"\t"$6"\t"$7}' > vcf_format

#headless clinvar
tail -n+2 $input  |  awk '{ print $1"\t"$2"\t"$4"\t"$5}' > vcf_format

##add VCF header
#cat vcf_header vcf_format > ${output}.FATHMM.vcf
cat vcf_format > ${output}.FATHMM.vcf

##change chromosome notations. e.g. 1 -> chr1.
#awk '{if($0 !~ /^#/) print "chr"$0; else print $0}' ${output}.FATHMM.vcf > ${output}.FATHMM.with_chr.vcf

#rm tmp vcf_format

rm vcf_format

#echo "complete"
