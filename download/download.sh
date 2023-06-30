#!/bin/bash

#David Rauch
#BCM MHG
#6/22/2023
#script to download a list of files saved in a .txt file

###

# download [file]
# reads a file and downloads the files on the txt file
# inputs:
# file: a .txt file containing only filenames
# output: a download of whatever file you called

function download() {

while read line; do
	echo "========================"
	echo "getting $line"
	wget -b $line # -b lets the downloads happen in the background
	echo "========================"
done < $1

}

download "$@"
