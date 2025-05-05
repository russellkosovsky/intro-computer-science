#gather eathquake data from the web and do some stats on it

from urllib.request import urlretrieve, urlopen
from urllib.parse import urlparse


class QuakeInfo:
    '''Class to read and process a url'''
    
    def __init__(self):
        self.url='http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson'
        
  
    def mean(self):
        urlFile = urlopen(self.url) #url file reference is an instance variable           
        totMag = 0
        numQuakes = 0
        
        #reads in first line of file (the column headers)
        line = urlFile.readline()
        #reads in secodn line of file (some notice)
        line = urlFile.readline()

        for line in urlFile:
            #your code here
            #print(line) # <-- good for testing, but to be removed

            #find position of "mag"
            ##your code

            #find position of comman immediately following the magnitude
            ##your code

            #slice magnitude value
            ##your code

            ###accumulator
            #convert magnitude to number and add to total
            ## your code

            #increment numQuakes by one
            ## your code

            ###if interested in region information
            ## how you can find region informaiton?
                      
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
    
