#gather eathquake data from the web and do some stats on it

from urllib.request import urlretrieve, urlopen
from urllib.parse import urlparse


class QuakeInfo:
    '''Class to read and process a url'''
    
    def __init__(self):
        self.url='http://earthquake.usgs.gov/earthquakes/catalogs/eqs7day-M1.txt'
        
  
    def mean(self):
        urlFile = urlopen(self.url) #url file reference is an instance variable           
        totMag = 0
        numQuakes = 0
        
        for line in urlFile:
            #your code here
            #print(line) # <-- good for testing, but to be removed

            #print(line) # <-- good for testing, but to be removed
            content = str(line)
            
            #find position of "mag"
            magpos = content.find('mag')

            #find position of comman immediately following the magnitude
            comma = content.find(',', magpos)

            #slice magnitude value
            magnitude = content[magpos+5:comma]
            print(magnitude)

            #convert magnitude to number and add to total
            totMag = totMag + eval(magnitude)
            numQuakes = numQuakes + 1

            #region? can you generate frequency ranking for regions
            place = content.find('place')
            of = content.find('of', place)
            comma = content.find(',', place)
            comma = content.find(',', comma+1)
            region = content[of+3:comma-1]
            print(region)
                      
        urlFile.close()

        ###compute average of accumulated magnitude. then return it
        
        #dummy code to return value
        return totMag/numQuakes

def main():
    #quakeinfo instance
    q = QuakeInfo()

    #compute mean magnitude
    avg = q.mean()

    #print result of mean
    print("Mean is:", avg)

if __name__ == "__main__":
    main()
    
