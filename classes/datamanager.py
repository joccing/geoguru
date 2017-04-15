#
# This class encapsulates the storage and retrieval of country data.

from dictionary import readDict, testDict, getDictName
from country import Country

class DataManager:
    
    def __init__(self, filename="", verbose=False, excludeList=[] ):
        self.__storeDB = readDict( filename, verbose, excludeList )

    def exclude(self, fieldsToRemove=[]):
        if len(self.__storeDB) == 0: return 0
        else:
            totalRemoved=0
            for f in fieldsToRemove:
                for countryName in self.__storeDB.keys():
                    if self.__storeDB[countryName].removePropertyExact(f): 
                        totalRemoved += 1
            return totalRemoved

    def getCountryApprox( self, countryRE ):
        import re
        result = []
        pattern = re.compile( ".*"+countryRE+".*", re.IGNORECASE )

        for countryName in self.__storeDB.keys():
            if pattern.match( countryName ):
                result.append( self.__storeDB[countryName] )

        return result

    def __str__(self):
        return "Number of records in DataManager: {0}".format(len(self.__storeDB))

    def getSize(self):
        return len(self.__storeDB)

if __name__ == '__main__':

    import os
    from command import cmd_load

    testDict("__testDict.tmp")

    dm = DataManager( "__testDict.tmp" )
    if dm.getSize() != 10: print("Error in creation of DataManager instance")
    if dm.exclude( ['Country','Rank'] ) != 20: print("Error in removal of property fields")
    r = dm.getCountryApprox( r'ch' )
    if len(r) < 1: print("Error in retrieving country objects by regex")

    dm = cmd_load( {'verbose':False}, ["__testDict.tmp",'Country','Rank'] )
    if dm.getSize() != 10: print("Error in creation through loadDataManager")
    r = dm.getCountryApprox( r'ch' )
    if len(r) < 1: print("Error in retrieving country objects by regex")

    os.remove( getDictName() )
    os.remove("__testDict.tmp")
