#!/bin/bash

LABNUM="05"
LAB="cpsc-120-lab-${LABNUM}"

#LOG="/tmp/runlog.$$.txt"
#GITBASE="${HOME}/github/cpsc120"
#PROMPT="cpsc-120-prompt-lab-${LABNUM}"
#SOLUTION="cpsc-120-solution-lab-${LABNUM}"
#BASE="/Users/mshafae/github/cpsc120/cpsc-120-solution-lab-${LABNUM}"

#echo "Logging output to ${LOG}."

for i in *-${LAB}-*; do
	pushd $i > /dev/null 2>&1
    make -j 2 test >& make_test_log.txt
	popd > /dev/null 2>&1
done

GRADING_LOG="grading_log.csv"
# Get the headers
head -1 `ls */.${LAB}_part-*.csv | head -1` > ${GRADING_LOG}
# Collect the rows
for i in *-${LAB}-*; do
    tail -q -n +2 ${i}/.${LAB}_part-*.csv >> ${GRADING_LOG}
done
