#pathToDocs = 'C:/Users/Christian/Documents/College schoolwork/Senior/Spring 2011/OPIM 311/Case3/UNGCCOPs'
#doc = 'eBayUNGCRr4final.txt'
#pathToQueryFile = 'C:/Users/Christian/Documents/College schoolwork/Senior/Spring 2011/OPIM 311/Case3/concepts/greenhouse_gases.txt'    
#pathToConceptFiles = 'C:/Users/Christian/Documents/College schoolwork/Senior/Spring 2011/OPIM 311/Case3/concepts'

def getDaFile(pathToDocs, doc):
    filenamePath = pathToDocs + '/' + doc
    daFile = open(filenamePath,'r')
    contents = daFile.read()
    daFile.close()
    return contents

#getDaFile(pathToDocs, doc)

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


import os

def report1(pathToDocs, pathToQueryFile):
## part 1 --- list of filenames under pathToDocs##
    dirList = os.listdir(pathToDocs)
    print dirList

## part 2 --- list of words in pathToQueryFile##
    os.path.split(pathToQueryFile)
    (filepath, queryfname) = os.path.split(pathToQueryFile)
    queryList = getDaFile(pathToDocs, queryfname).split()
    print queryList
    
## part 3 --- create output file and write headers ##
    myFile = open('output.txt','w')
    myFile.write('File' + ',' + queryfname)
    myFile.write('\n')
    
## part4 --- processing it all##
    for filename in dirList:
        print filename
        fileList = getDaFile(pathToDocs, filename).split()
        #print fileList
        daWordCount = 0
        for word in fileList:
            for item in queryList:
                if word == item:
                    daWordCount = daWordCount + 1
        print daWordCount
        myFile.write(filename + ',' + str(daWordCount))
        myFile.write('\n')
    return dirList
        
#report1(pathToDocs, pathToQueryFile)

##This function takes two arguments.
##pathToDocs is the full path to the folder containing
##the documents.
##pathToQueryFile is the full path to the file containing
##the query terms of interest.
##An example call is: report1(r’/Users/kimbrough/Dropbox/TextCollections/UNGCCOPs’, r’/Users/kimbrough/Dropbox/TextCollections/concepts/greenhouse_gases.txt’)
##The function:
##1.) Obtains a list of the filenames of the documents
##under pathToDocs.
##2.) Obtains as a list the words in the query file,
##pathToQueryFile.
##3.) Creates an output file, output.txt and writes
##header information to it:
##’File’ for the first column, the name of the
##query file in the second.
##Since output.txt is to be comma-separated,
##these are separated by ... a comma
##4.) For each document in the directory pathToDocs,
##gets the document as a string,
##converts the string to a list using split(),
##calculates the total number of
##occurrences of the words from the query file
##(concept list) appear in the document,
##and writes to output.txt a new line, consisting
##of the file name, followed by a comma,
##followed by the count of the number of occurrences
##of the words in the query file.


def report2(pathToDocs, pathToQueryFile, lowercase):
## part 1 --- list of filenames under pathToDocs##
    dirList = os.listdir(pathToDocs)
    print dirList

## part 2 --- list of words in pathToQueryFile##
    os.path.split(pathToQueryFile)
    (filepath, queryfname) = os.path.split(pathToQueryFile)
    queryList = getDaFile(pathToDocs, queryfname).split()
    print queryList
    
## part 3 --- create output file and write headers ##
    myFile = open('output.txt','w')
    myFile.write('File' + ',' + queryfname)
    myFile.write('\n')
    
## part4 --- processing it all##
    for filename in dirList:
        print filename
        fileString = getDaFile(pathToDocs, filename)
        if lowercase == True:
            loweredString = fileString.lower()
            loweredList = loweredString.split()
            #print loweredList
            daWordCount = 0
            for word in loweredList:
                for item in queryList:
                    if word == item:
                        daWordCount = daWordCount + 1
        elif lowercase == "":
            loweredString = fileString.lower()
            loweredList = loweredString.split()
            daWordCount = 0
            for word in loweredList:
                for item in queryList:
                    if word == item:
                        daWordCount = daWordCount + 1
        else:
            fileList = fileString.split()
            daWordCount = 0
            for word in fileList:
                for item in queryList:
                    if word == item:
                        daWordCount = daWordCount + 1
        print daWordCount
        myFile.write(filename + ',' + str(daWordCount))
        myFile.write('\n')
    return dirList
        
#report2(pathToDocs, pathToQueryFile, True)

##The function:
##1.) Obtains a list of the filenames of the documents
##under pathToDocs.
##2.) Obtains as a list the words in the query file,
##pathToQueryFile.
##3.) Creates an output file, output.txt and writes
##header information to it:
##’File’ for the first column, the name of the
##query file in the second.
##Since output.txt is to be comma-separated,
##these are separated by ... a comma
##4.) For each document in the directory pathToDocs,
##gets the document as a string,
##optionally (depending on lowercase)
##converts the file string to all lower case,
##converts the string to a list using split(),
##caculates the total number of
##occurrences of the words from the query file
##(concept list) appear in the document,
##and writes to output.txt a new line, consisting
##of the file name, followed by a comma,
##followed by the count of the number of occurrences
##of the words in the query file.


def report3(pathToDocs, pathToConceptFiles,lowercase):
## part 1 --- list of filenames under pathToDocs##
    dirList = os.listdir(pathToDocs)
    print dirList

## part 2 --- list of filenames in pathToConceptFiles##
    dirConceptList = os.listdir(pathToConceptFiles)
    print dirConceptList
      
## part 3 --- create output file and write headers ##
    myFile = open('output.txt','w')
    myFile.write('File_Name' + ',' + 'File_Length' + ',')
    for queryFileName in dirConceptList:
        myFile.write(queryFileName + ',')
    myFile.write('\n')
    
## part4 --- processing it all##
    queryCounter = 0
    for queryFile in dirConceptList:
        pathToQueryFile = pathToConceptFiles + '/' + queryFile
        (filepath, queryFileName) = os.path.split(pathToQueryFile) 
        wordList = getDaFile(pathToConceptFiles, queryFileName).split()
        print wordList
        fileCounter = 0
        for filename in dirList:
            
            print filename
            fileString = getDaFile(pathToDocs, filename)
            if lowercase == True:
                loweredString = fileString.lower()
                loweredList = loweredString.split()
                #print loweredList
                daWordCount = 0
                for word in loweredList:
                    for item in wordList:
                        if word == item:
                            daWordCount = daWordCount + 1
            elif lowercase == "":
                loweredString = fileString.lower()
                loweredList = loweredString.split()
                daWordCount = 0
                for word in loweredList:
                    for item in wordList:
                        if word == item:
                            daWordCount = daWordCount + 1
            else:
                fileList = fileString.split()
                daWordCount = 0
                for word in fileList:
                    for item in wordList:
                        if word == item:
                            daWordCount = daWordCount + 1
            print daWordCount
            
## part 5 --- writing to output file ##
            if queryCounter == 0:
                myFile.write(filename + ',' + str(len(fileString)) + ',' + str(daWordCount))
                myFile.write('\n')
            elif queryCounter == 1:
                if fileCounter == 0:
                    myFile.close()
                    myFile = open('output.txt','a')
                    myFile.write(','','',' + str(daWordCount))
                else:
                    myFile.write(','','',' + str(daWordCount))
                myFile.write('\n')
            elif queryCounter == 2:
                if fileCounter == 0:
                    myFile.close()
                    myFile = open('output.txt','a')
                    myFile.write(','','','',' + str(daWordCount))
                else:
                    myFile.write(','','','',' + str(daWordCount))
                myFile.write('\n')
            fileCounter = fileCounter + 1        
        queryCounter = queryCounter + 1
#report3(pathToDocs, pathToConceptFiles, True)


##The function:
##1.) Obtains a list of the filenames of the documents
##under pathToDocs.
##2.) Obtains a list of the filenames in the
##pathToConceptFiles directory.
##3.) Creates an output file, output.txt and writes
##header information to it:
##’File_Name’ for the first column,
##’File_Length" for the second column,
##the names of the
##concept files in the third and subsequent
##columns.
##Since output.txt is to be comma-separated,
##these are separated by ... a comma
##4.) For each concept in the directory
##pathToConceptFiles/, obtains as a list the
##words for the concept, then for each
##document in the directory pathToDocs,
##gets the document as a string,
##optionally (depending on lowercase)
##converts the file string to all lower case,
##converts the string to a list using split(),
##caculates the total number of
##occurrences of the words from the query file
##(concept list) appear in the document,
##and collects the results in a convenient
##data structure.
##5.) Drawing on the convenient data structure,
##writes to output.txt a new line for each
##source document, consisting
##of the file name, followed by a comma,
##followed by the length of the document and a comma,
##followed by the count of the number of occurrences
##of the words in each concept file.(Separated
##by commas.
