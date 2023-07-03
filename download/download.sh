#!/bin/bash

#David Rauch
#BCM MHG
#6/22/2023
#script to download a list of files saved in a .txt file

###

# download [inputs.txt]
# reads a file and downloads the files on the txt file
# inputs:
# file: a .txt file containing only filenames
# output: a download of whatever file you called

function download() {

counter=0

TARGET=$(wc -l $@ | cut -d ' ' -f 1)

while read line; do
	printf "\n========================"
	printf "\nworking on file $counter/$TARGET"
	printf "\n\ngetting $line\n\n"
	wget $line # downloads what I need
	printf "$line retreived\n"
	#wget -b $line # -b lets the downloads happen in the background
	printf "========================\n"
	
	counter=$((counter+1))

	if [[ $counter == $TARGET ]]; then
		printf "\n\n\n********************\n\nDownload completed\n\n********************\n\n"
	fi
done < $1

}

download "$@"
