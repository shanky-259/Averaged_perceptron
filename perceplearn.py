import json
import sys
import random
files=sys.argv

    
def classwords():
    allwordsset=set()
    classlist=[]
    for line in open(str(files[1]),"r",encoding='latin-1'):
        words=line.split()
        if words[0] not in classlist:
            classlist.append(words[0])
    for line in open(str(files[1]),"r"):
        words=line.split()
        for word in words:
            if word not in classlist:
                allwordsset.add(word)
    allwords=list(allwordsset)
    return classlist,allwords

def weights():
    global weight,weightavg
    weight={}
    weightavg={}
    for i in range(len(classlist)):
        weight[classlist[i]]={}
        weightavg[classlist[i]]={}
    for word in allwords:
        for i in range(len(classlist)):
            weight[classlist[i]][word]=0
            weightavg[classlist[i]][word]=0
            
def updateweight(feature,actualclass):
    predictedclass={}
    for i in range(len(classlist)):
        predictedclass[classlist[i]]=0
    for i in range(len(classlist)):
        for word in feature:
            predictedclass[classlist[i]]+=feature[word]*weight[classlist[i]][word]
    argmax=classlist[0]
    for key in predictedclass:
        if predictedclass[key]>predictedclass[argmax]:
            argmax=key
    if argmax!=actualclass:
        for word in feature:
            weight[argmax][word]-=feature[word]
            weight[actualclass][word]+=feature[word]
            
def train():
    N=10
    lines=[]
    for line in open(str(files[1]),'r'):
        lines.append(line)
    for i in range(N):
        for line in random.sample(lines,len(lines)):
            feature={}
            wordset=set()
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
            updateweight(feature,words[0])
        for eachclass in weight:
            for word in weight[eachclass]:
                weightavg[eachclass][word]+=weight[eachclass][word]      
    f1=open(str(files[2]),"w+")
    encode=json.dumps(weightavg)
    f1.write(encode)
    f1.close()        
        


classlist,allwords=classwords()
weights()
train()
