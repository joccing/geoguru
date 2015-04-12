#! /usr/bin/python3.4
#
# This program provides a simple command line too to query population statistics.
# Author: Tay Joc Cing
# Date: 20 Mar 2015
#

import sys
import os
sys.path.append( os.getcwd() + "/classes" )

from country import Country
from datamanager import DataManager
from command import CommandDispatcher

def main():

    from optparse import OptionParser
    usage = "usage: %prog [[option] <Country regex> [attribute regex]] "
    version = "0.5"

    parser = OptionParser( usage = usage, version="%prog " +version )
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Make lots of noise")
    parser.add_option("-f", "--file", action="store", dest="filename", help="Initialize store for country stats")
    (options, args) = parser.parse_args()

    dm = DataManager(options.filename, options.verbose, excludeList=['Country'])
    if len(args) < 1 and options.filename == None:
        # interactive mode
        CommandDispatcher( dm, options.verbose )
        
    else:
        # command line query mode
        if len(args) >= 1 and dm.getSize() > 0:

            # Find countries using regular expression match
            result = dm.getCountryApprox( args[0] )
            propertyRE = args[1] if len(args) == 2 else ""
            for c in result:
                print( c.getPropertyString(propertyRE) )

if __name__ == "__main__":
    main()
