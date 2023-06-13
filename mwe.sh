#!/bin/bash

set -x

#make a directory as an example, and place files inside
mkdir tmpdir
cd tmpdir
touch test1
touch test2
cd ..

# call fileclear
./fileclear.sh tmpdir
