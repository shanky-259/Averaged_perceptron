import json
import sys
import random
import time
from collections import defaultdict
files=sys.argv

class netrain:
    def __init__(self):
        pass
    
    def build1(self):
        lines=[]
        classes=set()
        allwordset=set()
        d={}
        for line in open(files[1],'r',errors='ignore'):
            wordlist=line.split()
            sentence='%%%BEGIN%%%'+' '
            for word in wordlist:
                sentence+=word.rsplit('/',1)[1]+' '
                sentence+=word.rsplit('/',1)[0]+' '
                classes.add(word.rsplit('/',1)[1])
            sentence+='%%%END%%%'
            lines.append(sentence)
        classlist=list(classes)
        return classlist,lines
    
    def updateweights(self,prevw,currentw,nextw,actualclass):
        predictedclass={}
        wordl=[prevw,currentw,nextw]
        for i in range(len(classlist)):
            predictedclass[classlist[i]]=0
        for i in range(len(classlist)):
            for word in wordl:
                try:
                    predictedclass[classlist[i]]+=feature[classlist[i]][word]*weight[classlist[i]][word]
                except:
                    predictedclass[classlist[i]]+=0
        argmax=classlist[0]
        for key in predictedclass:
            if predictedclass[key]>predictedclass[argmax]:
                argmax=key
        if argmax!=actualclass:
            weight[argmax][currentw]-=feature[actualclass][currentw]
            weight[actualclass][currentw]+=feature[actualclass][currentw]
    
    def train(self):
        N=1
        global weight,weightavg
        weight={}
        weightavg={}
        for eachclass in classlist:
            weight[eachclass]={}
            weightavg[eachclass]={}
        for i in range(N):
            for line in random.sample(lines,len(lines)):
                words=line.split()
                for index in range(2,len(words)-1,2):
                    global feature
                    feature={}
                    for i in range(len(classlist)):
                        feature[classlist[i]]={}
                    wprev='w_prev'+words[index-2]
                    wcurr='w_curr'+words[index]
                    try:
                        wnext='w_next'+words[index+2]
                    except:
                        wnext='w_next'+words[index+1]
                    relative=[wprev,wcurr,wnext]
                    for i in range(len(classlist)):
                        for eachword in relative:
                            feature[classlist[i]][eachword]=1
                            weight[classlist[i]][eachword]=0
                    p.updateweights(wprev,wcurr,wnext,words[index-1])
            
            for eachclass in weight:
                for word in weight[eachclass]:
                    try:
                        weightavg[eachclass][word]+=weight[eachclass][word]
                    except:
                        weightavg[eachclass][word]=weight[eachclass][word]
            
        f1=open(str(files[2]),"w+")
        encode=json.dumps(weightavg)
        f1.write(encode)
        f1.close()          
                    
if __name__== '__main__':
    t=time.time()
    p=netrain()
    classlist,lines=p.build1()
    p.train()
    print('seconds taken is %s : '%(time.time()-t))
    
