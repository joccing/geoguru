#! /usr/bin/python3.4
#
# This program provides a simple command line too to query population statistics.
# Author: Tay Joc Cing
#

import sys
import os
sys.path.append( os.getcwd() + "/classes" )

from country import Country
from datamanager import DataManager

def main():

    from optparse import OptionParser
    usage = "usage: %prog [option] <Country regex> [attribute regex] "
    version = "0.41"

    parser = OptionParser( usage = usage, version="%prog " +version )
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Make lots of noise")
    parser.add_option("-f", "--file", action="store", dest="filename", help="Initialize store for country stats")
    (options, args) = parser.parse_args()

    if len(args) < 1 and options.filename == None:
        parser.error("Invalid number of arguments")

    dm = DataManager(options.filename, options.verbose, excludeList=['Country'])

    if len(args) >= 1 and dm.getSize() > 0:

        # Find country using regular expression match
        result = dm.getCountryApprox( args[0] )
        propertyRE = args[1] if len(args) == 2 else ""

        for c in result:
            print( c.getPropertyString(propertyRE) )

if __name__ == "__main__":
    main()
