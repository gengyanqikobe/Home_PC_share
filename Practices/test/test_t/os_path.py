import os
from Practices.readConfig import proDir


#proDir = os.path.split(os.path.realpath(__file__))[0]

#print(proDir)

xlsPath = os.path.join(proDir,"testFile",'log.py')
print(xlsPath)

resultPath = os.path.join(proDir,'result')
print(resultPath)