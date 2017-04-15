#
# This contains commands for the interactive mode
# Author: Tay Joc Cing
# Date: 25 April 2015
#

from datamanager import DataManager
from constants import *

def cmd_hi( heapDict, args ):
    n = APP_NAME
    if args and len(args) > 0:
        n = args[0]
        print("Ok, my name shall be " + args[0])
    else:
        print("Welcome! I am %s!" % n)
    return n

def cmd_verbose( heapDict, args ):

    if args and len(args) > 0:
        return True if args[0] == 'on' else False
    else:
        return False

def cmd_quit( heapDict, args ):
    if heapDict.get( CMD_VERBOSE, False ):
        print( "Goodbye!" )
    return False

def cmd_cr( heapDict, args ):
    pass

def cmd_load( heapDict, args ):
    """ This method is used when called within the command line interactive mode"""
    verbose = heapDict.get('verbose',False)

    if args:
        fname = args[0] if len(args) > 0 else ""
        more = args[1:] if len(args) > 1 else []
        return DataManager( fname, verbose, more )
    else:
        if verbose: print("No arguments given!")
        return None

def cmd_query( heapDict, args ):
    """This function provides query capability to the command line interactive mode"""

    dm = heapDict.get('load',None)
    result = None

    if not dm:
        print( "No database loaded yet. Use 'load' command first.")
        return None

    if args and len(args) > 0:

        # Find countries using regular expression match
        result = dm.getCountryApprox( args[0] )

        # if no arguments, then assume all country stats are requested
        propertyRE = args[1] if len(args) == 2 else ""
        for c in result:
            print( c.getPropertyString(propertyRE) )

    # store countries of query match
    return result

    
