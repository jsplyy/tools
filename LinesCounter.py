#coding:utf-8

def block(file,size=65536):
    while True:
        nb = file.read(size)
        if not nb:
            file.close()
            break
        yield nb
def countFileLines(filename):
    with open(filename,"r") as f:
        return sum(line.count("\n") for line in block(f)) + 1

def countDirLines(filename):
    dirTotalLines = 0
    for root ,dirs,files in os.walk(filename):
        for dir in dirs:
            os.path.join(root,dir)
        for eachfile in files:
            eachCountFile = os.path.join(root,eachfile)
            print eachCountFile + ' Lines=' + str(countFileLines(eachCountFile))
            dirTotalLines = dirTotalLines + countFileLines(eachCountFile)
    return dirTotalLines
if __name__ == "__main__":
    import sys
    import os
    import os.path
    totalLines = 0
    errorInfo = '''
         Input error!
         please input config.txt or filename or dirname
         to be counted.
         '''
    if(len(sys.argv) != 2):
        print errorInfo
        sys.exit(-1)
    if(sys.argv[1]!="config.txt"):
        if(os.path.isfile(sys.argv[1])):
            print countFileLines(sys.argv[1])
        elif(os.path.isdir(sys.argv[1])):
            print countDirLines(sys.argv[1])
        else:
            print errorInfo
    else:
        configFile = open("config.txt","r")
        configLine = configFile.readline()
        while configLine:
            configLine = configLine.strip('\n')
            if(os.path.isdir(configLine)):
                totalLines += countDirLines(configLine)
            else:
                print configLine + ' Lines=' + str(countFileLines(configLine))
                totalLines = totalLines + countFileLines(configLine)

            configLine = configFile.readline()
        print "The number of the total Lines in config.txt is " + str(totalLines)