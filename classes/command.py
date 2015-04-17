#! /usr/bin/python3.4
#
# This is a command interpreter for interactive mode
# Author: Tay Joc Cing
# Date: 11 April 2015
#

from datamanager import cmd_load
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

################################################################################

__commands = {

    CMD_HI: cmd_hi,
    CMD_LOAD: cmd_load,
    CMD_VERBOSE: cmd_verbose,
    CMD_QUIT: cmd_quit,
    CMD_CR: cmd_cr
}

__results = {}

###############################################################################

def CommandDispatcher( commands=__commands, cursor=IM_PROMPT ):

    while __results.get( CMD_QUIT, True ):

        __commandStr = input(IM_PROMPT+" ").strip()
        __tokens = extract(__commandStr)

        if __tokens[0] in __commands.keys():
            __results[__tokens[0]] = __commands[__tokens[0]]( __results, __tokens[1:] if len(__tokens) > 1 else None)
        else:
            print("Command '%s' not found!" % __tokens[0])

def extract( s ):
    """Extract tokens from an input string"""
    return s.lower().split(" ")

if __name__ == '__main__':
    CommandDispatcher()
