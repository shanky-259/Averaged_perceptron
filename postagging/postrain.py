import sys
from perceplearn import train
files=sys.argv

    
def build1():
    lines=[]
    classes=set()
    allwordset=set()
    d={}
    for line in open(files[1],'r'):
        wordlist=line.split()
        sentence='%%%BEGIN%%%'+' '
        for word in wordlist:
            sentence+=word.split('/')[1]+' '
            sentence+=word.split('/')[0]+' '
            classes.add(word.split('/')[1])
        sentence+='%%%END%%%'
        lines.append(sentence)
    classlist=list(classes)
    train(classlist,lines)
    
build1()
    
