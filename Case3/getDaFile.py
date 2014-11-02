pathToDocs = 'C:/Users/Christian/Documents/College schoolwork/Senior/Spring 2011/OPIM 311/Case3'
doc = 'eBayUNGCRr4final.txt'
    
def getDaFile(pathToDocs, doc):
    filename = pathToDocs + '/' + doc
    
    getDaFile = open(filename,'r')
    lines = getDaFile.readlines()
    for line in lines:
        print(line.strip())
    getDaFile.close()  

getDaFile(pathToDocs, doc)

##This function accepts two arguments:
##pathToDocs is the full path to the
##directory in which the documents lie.
##doc is the file name of the document
##to be gotten, presumed to be in the
##directory.
##The function opens the file, reads it
##and returns the contents as a string
##for subsequent processing. The function
##was built for and tested on the
##UNGOCOPs/ documents and works in both
##Python 2.6X and Python 3.
