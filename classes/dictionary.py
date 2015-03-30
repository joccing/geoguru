#! /usr/bin/python3.4

if __name__ == '__main__':
    from country import Country
    import os
else:
    from classes.country import Country

def createDict( filename, verbose=False ):
    """ Read and construct dictionary of country population statistics """

    cdict = {}
    with open(filename,"r") as f:
        fields = f.readline().replace(",","").strip()
        fieldsList = fields.split(' ')

        # Read in country data to form dictionary
        for line in f:
            statsList = line.strip().split(' ')
            if len(statsList) != len(fieldsList):
                print("Mismatch error in fields and country data!")
                break
            else:
                if statsList[1] not in cdict:
                    cdict[statsList[1]] = Country( statsList[1], dict(zip(fieldsList,statsList)) )
                else:
                    print("Error: {0} duplicate found!".format( statsList[1] ) )

    if verbose == True:
        print("Country dictionary created with %d entries." % len(cdict))

    return cdict

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
11 Mexico 123799215 1.20 1466816 -267202 27.3 10 2.23 1958198 63 79 97734761 1.71
12 Philippines 100096496 1.73 1702922 -156793 23.2 7 3.11 300000 334 50 49643960 1.38
13 Ethiopia 96506031 2.56 2405275 -11577 18.4 5 4.72 1104302 87 18 17172948 1.33
14 Vietnam 92547959 0.95 868226 -53768 30.3 10 1.78 331689 279 33 30482811 1.28
15 Egypt 83386739 1.62 1330361 -47438 25.5 9 2.82 1001450 83 44 36713659 1.15
16 Germany 82652256 -0.09 -74370 42856 45.9 28 1.40 357021 232 74 61437197 1.14
17 Iran 78470222 1.32 1023054 -67715 29.0 8 1.92 1648188 48 70 54547946 1.08
18 Turkey 75837020 1.21 904379 -47433 29.8 11 2.07 783562 97 74 56235478 1.05
19 Congo 69360118 2.73 1846441 -11941 17.4 5 6.08 2344832 30 36 24912419 0.96
20 Thailand 67222972 0.32 212470 -29600 37.4 15 1.42 513113 131 35 23691532 0.93"""
    with open(filename,"w+") as f:
        f.write(s)
    return f

if __name__ == '__main__':
    testDict("_testDict.tmp")
    if len(createDict( "_testDict.tmp")) != 20: print("Error encountered with testDict")
    os.remove("_testDict.tmp")

