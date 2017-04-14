#! /usr/bin/python3.4
#
# This program provides a simple command line to query population statistics.
# Author: Tay Joc Cing
# Date: 20 Mar 2015
#

import sys
import os

from country import Country
from datamanager import DataManager
from dispatcher import CommandDispatcher
from constants import *

sys.path.append(os.getcwd() + "/classes")

def main():

    from optparse import OptionParser
    usage = "usage: %prog [[option] <Country regex> [attribute regex]] "
    version = APP_VERSION

    parser = OptionParser(usage=usage, version="%prog " + version)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
                            default=False, help="Make lots of noise")
    parser.add_option("-f", "--file", action="store", dest="filename",
                            help="Initialize store for country stats")
    (options, args) = parser.parse_args()

    if len(args) < 1 and options.filename is None:
        # interactive mode
        CommandDispatcher()
    else:
        dm = DataManager(options.filename, options.verbose,
                         excludeList=['Country'])

        # command line query mode
        if len(args) >= 1 and dm.getSize() > 0:

            # Find countries using regular expression match
            result = dm.getCountryApprox(args[0])

            # if no arguments, then assume all country stats are requested
            propertyRE = args[1] if len(args) == 2 else ""
            for c in result:
                print(c.getPropertyString(propertyRE))

if __name__ == "__main__":
    main()
