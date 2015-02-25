import sys
import json
import codecs
files=sys.argv
sys.stdin = codecs.getreader('latin-1')(sys.stdin.detach())


def loadmodell():
    f=open(str(files[1]),'r',encoding='latin-1')
    weightavg=json.loads(f.read())
    return weightavg

def classify(classlist):
    for line in sys.stdin.readlines():
        percepclassify(line,classlist,weightavg)

def percepclassify(line,classlist,weightavg):
    output=''
    words=line.split()
    feature={}
    wordset=set()
    classify={}
    words=line.split()
    for word in words:
        if word not in classlist:
            wordset.add(word)
    trainingeg=list(wordset)
    for word in trainingeg:
        feature[word]=0
    for word in words:
        if word not in classlist:
            feature[word]+=1
    for eachclass in classlist:
        classify[eachclass]=0
    for eachclass in classlist:
        for eachword in feature:
            try:
                classify[eachclass]+=feature[eachword]*weightavg[eachclass][eachword]
            except:
                classify[eachclass]+=0
    maximum=classlist[0]
    for eachclass in classlist:
        if classify[eachclass]>classify[maximum]:
            maximum=eachclass
    print(maximum)
    
    
weightavg=loadmodell()
classlist=[]
for key in weightavg:
    classlist.append(key)
classify(classlist)
    



    
    
