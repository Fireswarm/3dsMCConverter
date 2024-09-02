def convertNameBE(namePath):
    #needs to read name from file
    nameFile = open(namePath, "r")
    readName = nameFile.read()
    nameFile.close()
    return readName

def translateLevelDataBE(levelPath, oldLevelPath):
    #needs to read and interpret data from level files
    levelData = []

    #first read in regular levelData
    levelFile = open(levelPath, "rb")
    levelData.append(levelFile.read())
    levelFile.close()

    #now the old levelData
    levelFile = open(oldLevelPath, "rb")
    levelData.append(levelFile.read())
    levelFile.close()
    
    return levelData

def parseDB(dbFolder):
    readDatabase = "A bunch of junk that we unpack"
    return readDatabase

def readBEFile(filepath):
    #Conver World Metadata
    convertNameBE(filepath+"/levelname.txt")
    translateLevelDataBE(filepath+"/level.dat", filepath+"level.dat_old")

    #Convert DataBase
    parseDB(filepath+"/db")

