#!/bin/bash

# David Rauch
# BCM MHGCP
# 7/3/2023

###

# ghcommit.sh [message]

# commit the current working directory and pushes it to GitHub
# inputs:
# message (optional) - the message for your commit to GitHub
# output:
# a push of the commit to GitHub

# Usage: call this in the directory for the repo you are committing to. 


function ghcommit() {

cwd=${pwd}

git add $cwd

# check to see if we already have entered a commit message
#if [ ${#} -gt 0 ]; then
#	read -p "Enter commit message: " msg
#	git commit -m $msg
#
#else 
#	git commit -m "$@"
#fi

#read -p "Enter commit message: " msg

echo "Enter commit message:"
read -r $msg

git commit -m "$msg"

git push

}

ghcommit "$@"
