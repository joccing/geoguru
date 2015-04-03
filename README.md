# geoguru 0.2

Project to create a database of country specific statistics that can be queried

It takes a text file of country specific data and I have writen a Python program to allow command-line query of any country and for any of its attributes, such as population size or density per km2.

Step 1: Prepare country data

I simply copied and paste the data from Worldometer's page on country population statistics, into a text file.  The file clean.sh takes two arguments, this raw data file and the raw data file that contains the field names.  The output is a cleaned up version, properly formatted to be loaded into the main program.  The result will be sstored in data.out

$ cd raw
$ clean.sh world-population.raw fields
$ head data.out

Step 2: Load data file into main DB

The main program currently takes the output of step 1 and creates a memory store that can be queried by country name and attribute.  For instance to query about Uruguay's geo statistics:

$ cmain.py -f raw/data.out Uruguay

or if you can't remember the whole name,

$ cmain.py -f raw/data.out urug

To find all statistics that involve the substring 'pop'

$ cmain.py -f raw/data.out urug pop

Version History
===============

v0.2	Use Python Pickle module and hide raw/data.out from command line if not provided.
v0.3	To add logic for  dependency on -f option and if pickle file is found.
v0.31	Replaced pickle with shelve instead.  Updated test code in dictionary.py