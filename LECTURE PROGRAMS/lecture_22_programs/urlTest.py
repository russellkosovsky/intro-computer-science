#url test - open a web page for examination

import os
import platform

from urllib.request import urlretrieve, urlopen
from urllib.parse import urlparse

class URLReader:
    '''Class to read and process a URL'''
    def __init__(self, urlString):
        '''set the URL of interest'''
        self.url = urlString
        
    def saveURL(self, fileName):
        '''save the html of the web page to a text file for later processing'''
        urlretrieve(self.url, fileName)
        #here, the urlparse method returns a tuple that splits up the url into components
        print ('The protocol is', urlparse(self.url)[0])
        print ('The net locator is', urlparse(self.url)[1])
        print ('The path is', urlparse(self.url)[2])

    def openURL(self):
        '''extract the title of the web page, printing it and creating an instance variable to hold it'''
        urlFile = urlopen(self.url)
        #now you have a pointer to a file -- it can be used just like a regular infile variable
        #in the sense that it has the same .read(), .readline(), and .readlines() methods
        #print (urlFile.geturl())  #shows that you can also get the URL of the file

        ## your code for part 2 goes here ##

        ## read contents of the page and store it to webpagecode string
        webpagecode = str(urlFile.read())
        #print(webpagecode)

        ## find <title> tag: use find() method of string
        start = webpagecode.find('<title>')
        end = webpagecode.find('</title>')
        
        ## string slicing to extract title
        print(webpagecode[start+7:end])
        self.title = webpagecode[start+7:end]
        
        #close url file
        urlFile.close()


    def openBrowser(self, urlString):
        '''open the webpage with system's default web browser'''
        #depend on operating system (Mac, PC, or Linux)
        if platform.system() == 'Windows':
            os.startfile(urlString)
        elif platform.system() == 'Darwin':
            os.system(('open ' + urlString))
        else:   #Linux?
            try:
                subprocess.Popen(['xdg-open', url])
            except OSError:
                print('Failed to open a browser!')

    ###your code for part 3 goes here: write displayTitle method
    def displayTitle(self):
        # open output file
        outputFile = open('sample.html', 'w')

        ### create string with simple html page with some title
        #i.e. <html><body><html> <body> The title of the web page is <i>"+self.title+"</i></body></html>

        ### write the string to output file
        #i.e. outputFile.write(html_content_string)
        
        # close output file
        outputFile.close()

        ### open saved webpage file via openBrowser method
        #i.e. self.openBrowser(html_file_name or url)
    

    ###fun part: email hunter
    def collectEmail(self, urlString):
        #open url file
        urlFile = urlopen(urlString)

        ### read all webpage contents and store it in webpagecode string
        webpagecode = str(urlFile.read())
        
        ### close urlFile
        urlFile.close()
        
        ### search for mailto tag
        start = webpagecode.find('mailto')
        end = webpagecode.find("\"", start)

        email = webpagecode[start+7:end]
        print(email)

        
        ### return email address
        return email
        
def main():
    #testing out the URLReader class we defined above
    myUrl=URLReader('http://www.google.com')
    #myUrl=URLReader('http://www.xkcd.com/664/')  #go here for a funny comic =)
    #myUrl.saveURL('urlTestfile.txt')
    #myUrl.openURL()
    #myUrl.displayTitle()

    #email bot
    email = myUrl.collectEmail('http://oak.conncoll.edu/james-lee/mail.html')
    print('email', email, 'collected!')
     
if __name__ == "__main__":
    main()
