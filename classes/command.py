#! /usr/bin/python3.4
#
# This contains commands for the interactive mode
# Author: Tay Joc Cing
# Date: 25 April 2015
#

from datamanager import DataManager
from constants import *

class cmd_root(object):

    err = {
        100: "Incorrect number of arguments"
    }

    def __init__(self, name, args, errcode = None ):
        self.__name = self.__class__.__name__.split("_")[1]
        self.__args = args
        if errcode:
            for code in errcode.keys():
                cmd_root.err[code] = errcode[code]

    def doit( self, heap, args ):
        return self.IsArgsValid( args )

    def IsArgsValid( self, argsList ):
        if argsList and len(argsList) >= self.__args:
            return True
        else:
            return False

    def ErrorHandler( self, code ):
        print( self.__class__.__name__ + ": " + cmd_root.err.get( code, "Unknown error code encountered" ))
        return False
        

class cmd_hi( cmd_root ):

    def doit( self, heap, args ):

        if super().doit( heap, args ):

            print("Welcome! I am %s!" % APP_NAME)
            return True
        else:
            return self.ErrorHandler( 100 )
        
        
"""
def cmd_hi( heapDict, args ):
    n = APP_NAME
    if args and len(args) > 0:
        n = args[0]
        print("Ok, my name shall be " + args[0])
    else:
        print("Welcome! I am %s!" % n)
    return n
"""

class cmd_verbose( Command ):

    __errcode = {
        200: "Invalid argument values"
    }

    def __init__(self):
        super().__init__("verbose", 1, __errcode )

    def doit( self, heap, args ):

        if self.IsArgsValid( args ):

            if args[0] == 'on':
                return True
            elif args[0] == 'off':
                return False
            else:
                return self.ErrorMessage( self.__class__.__name__, 200 )
        else:
            return self.ErrorMessage( self.__class__.__name__, 100 )

"""
def cmd_verbose( heapDict, args ):

    if args and len(args) > 0:
        return True if args[0] == 'on' else False
    else:
        return False
"""

class cmd_quit( Command ):

    def __init__(self):
        super().__init__("exit", 0 )

    def doit( self, heap, args ):

        if self.IsArgsValid( args ):
            if heap.get( CMD_VERBOSE, False ): print( "Goodbye!" )
            return False
        else:
            return self.ErrorMessage( self.__class__.__name__, 100 )

"""
def cmd_quit( heapDict, args ):
    if heapDict.get( CMD_VERBOSE, False ):
        print( "Goodbye!" )
    return False
"""

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

    
