
import pickle
from country import Country

PICKLE_FILE= "_countries.pick"

def createDict( filename, verbose=False, excludeList=[] ):
    """ Read and construct dictionary of country population statistics """

    cdict = {}

    try:
        f = open(filename, "r")
    except IOError:
        print( "Error reading file:", filename)
    else:
        with f:
            fields = f.readline().replace(",","").strip()
            fieldsList = fields.split(' ')

            # Read in country data to form dictionary
            for line in f:
                statsList = line.strip().split(' ')
                if len(statsList) != len(fieldsList):
                    print("Mismatch error in fields and country data!")
                    break
                else:
                    # check if this country has already been added earlier
                    if statsList[1] not in cdict:

                        propertyDict = dict(zip(fieldsList,statsList))
                        for field in excludeList:
                            if field in propertyDict: del propertyDict[field]

                        # Store Country object into the dictionary using its name as key
                        cdict[statsList[1]] = Country( statsList[1], propertyDict )
                    else:
                        if verbose: print("Error: {0} duplicate found!".format( statsList[1] ) )

    return cdict

def storeDict( cdict ):

    try:
        fhandle = open( PICKLE_FILE, "wb" )
        pickle.dump( cdict, fhandle )
    except:
        print("Error in creating cached DB")
        return False
    finally:
        fhandle.close()

    return True

def readDict( filename, verbose=False, excludeList=[] ):

    cdict={}
    if filename and filename.strip():
        # priority is to use option file first 
       cdict = createDict( filename, verbose, excludeList )

       # check for error with given filename, if none, store results
       # else try to retrieve from cached file
       if cdict and storeDict( cdict ):
           print("New country DB has %d entries." % len(cdict))
       else:
           return readDict("", verbose, excludeList )
    else:
        if verbose: print("Trying cached DB file..")
        try:
            fhandle = open( PICKLE_FILE, "rb" )
            cdict = pickle.load( fhandle )
            fhandle.close()
        except FileNotFoundError:
            if verbose: print( "No cached DB file found" )
        except:
            import sys
            print( "\nUnexpected error:", sys.exc_info()[0] )
            raise
        else:
            if len(cdict) > 0: 
                print("Using cached DB with %d entries." % len(cdict))
            else:
                # detected empty cached file, so remove it
                import os
                os.remove( PICKLE_FILE )
                if verbose: print( "Unable to use cached DB")

    return cdict

def getDictName():
    return PICKLE_FILE

def testDict(filename):
    s="""Rank, Country, Population_2014, 1_Year_Change, Population_Change, Migrants_net, Median_Age, Aged_60+, Fertility_Rate, Area_km2, Density_P/km2, Urban_Pop_%, Urban_Population, Share_of_World_Pop
1 China 1393783836 0.59 8217299 -313996 35.7 14 1.66 9596947 145 54 756300115 19.24
2 India 1267401849 1.22 15262253 -483402 26.6 9 2.53 3287265 386 32 410404773 17.50
3 U.S.A. 322583006 0.79 2532290 1008835 37.5 20 1.99 9629056 34 83 268084524 4.45
4 Indonesia 252812245 1.18 2946614 -141488 28.1 8 2.38 1904567 133 53 133860626 3.49
5 Brazil 202033670 0.83 1671745 -46113 30.7 12 1.83 8514209 24 85 172549088 2.79
6 Pakistan 185132926 1.64 2990332 -334980 22.8 7 3.30 796096 233 37 68888535 2.56
7 Nigeria 178516904 2.82 4901559 -60000 17.8 4 6.01 923766 193 51 91834051 2.46
8 Bangladesh 158512570 1.22 1917608 -456443 25.4 7 2.24 143998 1101 30 47334620 2.19
9 Russia 142467651 -0.26 -366038 254018 38.4 19 1.51 17076310 8 74 105911587 1.97
10 Japan 126999808 -0.11 -143769 73466 46.2 33 1.40 377873 336 93 117995650 1.75
"""
    with open(filename,"w+") as f:
        f.write(s)
    return f

if __name__ == '__main__':
    import os
    testDict("_testDict.tmp")
    d = readDict( "_testDict.tmp", excludeList=['Country','Rank'] )
    if len(d) != 10: print("Error encountered with testDict")
    if len(d['Brazil'].getPropertyString().split(',')) != 13: print("Error encountered with exclusion of fields")
    os.remove("_testDict.tmp")
    d = readDict( "" )
    if len(d) != 10: print("Error encountered with readDict")
    os.remove( getDictName() )

