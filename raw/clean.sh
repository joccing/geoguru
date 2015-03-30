#! /bin/bash
#
# Cleans up population data obtained from a screen copy from worldometer.
# Author: Tay Joc Cing
# 10 Mar 2015

if [ $# -lt 2 ]
then
	echo Processes data copied directly from population by country data from Worldometers.
	echo Usage: clean \<raw file\> \<output file\>
	exit;
fi

sed '/^[0-9][0-9]*$/d' $1 | sed -n '/^[A-Z].*$/p' | sed 's/ /_/g' > tmp1
sed -n '/^[0-9].*$/s/[,%$]//gp' < $1 | sed -n 's/\t/ /gp' | sed -n 's/  */ /gp' > tmp2
rm -f data.out
cp $2 data.out
join <(nl tmp1) <(nl tmp2) >> data.out
rm tmp1 tmp2
echo "Data extracted and stored in data.out"
