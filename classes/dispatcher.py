#! /usr/bin/python3.4
#
# This is a command interpreter for interactive mode
# Author: Tay Joc Cing
# Date: 11 April 2015
#

from command import cmd_hi, cmd_load, cmd_verbose, cmd_quit, cmd_cr, cmd_query
from constants import *

__commands = {

    CMD_HI: cmd_hi,
    CMD_LOAD: cmd_load,
    CMD_VERBOSE: cmd_verbose,
    CMD_QUIT: cmd_quit,
    CMD_CR: cmd_cr,
    CMD_QUERY: cmd_query
}

__results = {}

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
