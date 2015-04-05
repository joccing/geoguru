#! /usr/bin/python3.4

"""
This is a system to query statistics for a country by approximate name match.

Author: Tay Joc Cing
Date: 10 Mar 2015

Version: 0.1
"""

class Country:
    """ 
    This is a class to capture statistics for a country 

    >>> from country import Country
    >>> c = Country("Singapore", {"Population":5000000, "Density_km2": 800.2, "Weather":"Tropical"})
    >>> print(c.getPropertyExact("Population"))
    {'Population': 5000000}
    >>> print(c.getPropertyApprox(r'Den'))
    {'Density_km2': 800.2}
    >>> c.setPropertyExact("Weather","Sunny")
    True
    >>> c.setPropertyExact("Main_Industry","Argriculture")
    False
    >>> print(c.getPropertyExact("Weather"))
    {'Weather': 'Sunny'}
    >>> x = Country("India",{"Size":23440,"Weather":"Spring"})
    >>> print(x.getPropertyString("iz"))
    Name: India, Size: 23440
    >>> x = Country("India",{})
    >>> print(x)
    Name: India
    >>>
    """
    
    def __init__(self, name, properties={}):
        self.__name = str(name)
        self.__properties = properties
    
    def __str__(self):
        return self.getPropertyString()

    def getPropertyString(self, regexp=""):
        """ Formats the information required in a pleasing way """
        if regexp:
            attributeDict = self.getPropertyApprox(regexp)
        else:
            attributeDict = self.getPropertyApprox(r'.*')

        s = "Name: " + self.__name
        if attributeDict:
            s += ", "
            s += str(attributeDict).strip("{}").replace("'","")

        return s

    def getPropertyExact(self,x, *key):
        key = (x,) + key
        return {k:self.__properties[k] for k in key if k in self.__properties}

    def getPropertyApprox(self, regexp):
        """ This method will do a search 
        of keys using a regular expression raw string """
        import re

        matches = {}
        pattern = re.compile( ".*"+regexp+".*", re.IGNORECASE )

        for k in self.__properties:
            if isinstance( k, str) and pattern.match( k ):
                matches[k] = self.__properties[k]

        return matches

    def setPropertyExact(self, key, value):
        if key in self.__properties:
            self.__properties[key] = value
            return True
        else:
            return False

    def removePropertyExact(self, key):
        if key in self.__properties:
            del self.__properties[key]
            return True
        else:
            return False

if __name__ == '__main__':

    import doctest
    doctest.testmod()
