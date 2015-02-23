import sys
import json
from percepclassify import percepclassify
files=sys.argv

    
def loadmodell():
    f=open(str(files[1]),'r')
    weightavg=json.loads(f.read())
    return weightavg

def classify(classlist):
    lines=sys.stdin.readline()
    output=''
    wordss=lines.split()
    line='%%%BEGIN%%%'+' '
    for word in wordss:
        line+=word+' '
    line+='%%%END%%%'
    percepclassify(line,classlist,weightavg)
            

weightavg=loadmodell()
classlist=[]
for key in weightavg:
    classlist.append(key)
classify(classlist)
