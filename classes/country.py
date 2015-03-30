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
    >>> c.setProperty("Weather","Sunny")
    True
    >>> c.setProperty("Main_Industry","Argriculture")
    False
    >>> print(c.getPropertyExact("Weather"))
    {'Weather': 'Sunny'}
    >>>
    """
    
    def __init__(self, name, properties={}):
        self.__name = name
        self.__properties = properties
    
    def __str__(self):
        text = "Country Name:" + self.__name + "\n"
        for key in self.__properties:
            text += "{0}: {1}\n".format(key,self.__properties[key] )
        return text

    def getPropertyExact(self,x, *key):
        key = (x,) + key
        return {k:self.__properties[k] for k in key if k in self.__properties}

    def getPropertyApprox(self, regexp):
        """ This method will do a search 
        of keys using a regular expression raw string """
        import re

        matches = {}
        for k in self.__properties:
            if isinstance(k,str) and re.search( regexp, k ):
                matches[k] = self.__properties[k]
        return matches

    def setProperty(self, key, value):
        if key in self.__properties:
            self.__properties[key] = value
            return True
        else:
            return False

if __name__ == '__main__':

    import doctest
    doctest.testmod()

#    c = Country("Singapore", {"Population":5000000, "Density_km2": 800.2, "Weather":"Tropical"})
#    print(c,end="")
#    print(c.getPropertyExact("Population"))
#    print(c.getPropertyApprox(r'e'))
