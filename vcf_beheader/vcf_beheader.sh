#!/bin/bash

function vcf_beheader(){

awk '! /\##/' $1  > beheaded_${1}.vcf

}

vcf_beheader "$@"
