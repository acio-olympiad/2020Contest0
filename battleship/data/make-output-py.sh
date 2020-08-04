#!/bin/bash
# NOTE: Modified to be used with Python3

echo "Compiling judge solutions..."

declare -a soln
for i in ../solutions/*-full.py; do
	echo $i
	soln+=$i
done

echo "Done"

echo "Generating output files and/or testing judge solutions"

for sol in ${soln[@]}; do
    echo "-------------------"
    echo "Testing $sol"
    echo "-------------------"
    for input in *.in; do
        output=${input%in}out

        if [ -e $output ]; then
            
            echo -n "Test $input "
            python3 $sol < $input > temp
            diff -b temp $output > /dev/null
            if [ $? -eq 0 ]; then
                echo "correct"
            else
                echo "incorrect"
                #diff -b temp $output
            fi
        else
        
            echo "$output does not exist. Generating it now..."
            python3 $sol < $input > $output
            if [ $? -ne 0 ]; then
                rm $output
            fi
        fi
    done
done

if [ -e temp ]; then
    rm temp
fi
