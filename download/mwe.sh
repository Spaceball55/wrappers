#!/bin/bash

touch inputs.txt

# place items to download into inputs.txt
echo "github.com" > inputs.txt
echo "http://some_file.tar.gz" > inputs.txt 

./download inputs.txt
