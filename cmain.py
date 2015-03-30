#! /usr/bin/python3.4
#
# This program provides a simple command line too to query population statistics.
# Author: Tay Joc Cing
#

from classes.country import Country
from classes.dictionary import createDict

def main():

    from optparse import OptionParser
    usage = "usage: %prog [option] countries"
    version = "0.1"

    parser = OptionParser( usage = usage, version="%prog " +version )
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Make lots of noise")
    parser.add_option("-f", "--file", action="store", dest="filename", help="Initialize shelve for country stats")
    (options, args) = parser.parse_args()

    if len(args) < 1 and options.filename == None:
        parser.error("Invalid number of arguments")

    if options.filename != None:
        cdict = createDict( options.filename, options.verbose )

        if len(args) >= 1:

            # Process country queries
            if options.verbose == True:
                print("Retrieving information about " + args[0] + "...") 
            
            if args[0] in cdict:

                country = cdict[args[0]]
                stats = country.getPropertyApprox(r'.*')
                print("%s:" % args[0] )
                print(stats)

            else:
                print("No such country found!")

if __name__ == "__main__":
    main()
