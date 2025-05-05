#gather eathquake data from the web and do some stats on it

from urllib.request import urlretrieve, urlopen
from urllib.parse import urlparse

class QuakeInfo:
    
    '''Class to read and process a url'''
    def __init__(self):
        self.url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson'
        
    def mean(self):
        urlFile = urlopen(self.url) #url file reference is an instance variable           

        totMag = 0
        numQuakes = 0
        maxMag = 0
        for line in urlFile:
            line = str(line)
            magPos = line.find("mag")
            commaPos = line[magPos:].find(",")
            #print("commaPos: ", commaPos)
            #print()
            #print("line[magPos]: ", line[magPos])

            mag = line[magPos+5:magPos+commaPos]
            #print(mag) # <-- good for testing, but to be removed
            #print(type(line))
            mag = eval(mag)

            if mag > maxMag:
                maxMag = mag

            totMag = totMag + mag
            numQuakes = numQuakes + 1

        print("Average: ", totMag/numQuakes)
        print()
        print(max(totMag / numQuakes))
        print()
        print("Max: ", maxMag)
        urlFile.close()


def main():
    
    qi = QuakeInfo()
    qi.mean()

main()























