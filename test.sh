#!/bin/bash

for i in $( find . -name "tests.py" -type f)
	do python $i
done	
