#! /usr/bin/python3.4
#
# This program provides a simple command line too to query population statistics.
# Author: Tay Joc Cing
#

from classes.country import Country
from classes.dictionary import createDict, readDict

def main():

    from optparse import OptionParser
    usage = "usage: %prog [option] <Country Name> [attribute] "
    version = "0.1"

    parser = OptionParser( usage = usage, version="%prog " +version )
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Make lots of noise")
    parser.add_option("-f", "--file", action="store", dest="filename", help="Initialize shelve for country stats")
    (options, args) = parser.parse_args()

    if len(args) < 1 and options.filename == None:
        parser.error("Invalid number of arguments")

    cdict = readDict( options.filename, options.verbose, excludeList=['Country'] )

    if len(args) >= 1 and cdict:

        # Find country using regular expression match
        import re
        pattern = re.compile( ".*"+args[0]+".*", re.IGNORECASE )

        for countryName in list(cdict.keys()):
            m = pattern.match( countryName )
            if m:
                if options.verbose == True: print("Found",countryName,"...")
                country = cdict[countryName]

                if len(args) == 2:
                    print(country.getPropertyString(args[1]))
                else:
                    print(country)            

if __name__ == "__main__":
    main()
