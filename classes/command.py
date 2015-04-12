#! /usr/bin/python3.4
#
# This is a command interpreter for interactive mode
# Author: Tay Joc Cing
# Date: 11 April 2015
#

__Greeting = "Command line interpreter v1.0"
__Cursor = ">>>"
__exitCommand = "exit"

def sayHello( options ):
    print("Hello World! - " + repr(options))

__commands = {
    "hi": sayHello
}

def CommandDispatcher( verbose=False, commands=__commands, greeting=__Greeting, cursor=__Cursor, exitCommand=__exitCommand ):
    
    if verbose: print(__Greeting)
    while True:

        __commandStr = input(cursor+" ").strip()
        __tokens = extract(__commandStr)

        if __tokens[0].lower() == exitCommand: 
            if verbose: print( "Goodbye!" )
            break
        elif __tokens[0] == '':
            continue
        else:
            if __tokens[0] in __commands.keys():
                __commands[__tokens[0]](__tokens[1:] if len(__tokens) > 1 else "No arguments")
            else:
                print("Command '%s' not found!" % __tokens[0])

def extract( s ):
    """Extract tokens from an input string"""
    return s.split(" ")

if __name__ == '__main__':
    CommandDispatcher( True )
