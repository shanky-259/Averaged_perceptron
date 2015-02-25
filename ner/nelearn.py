import sys
import random
import json
files=sys.argv


def build():
    lines=[]
    classes=set()
    allwordset=set()
    for line in open(files[1],'r',encoding='latin-1'):
        wordlist=line.split()
        sentence='%%%BEGIN%%%'+' '
        for word in wordlist:
            sentence+=word.rsplit('/',1)[1]+' '
            sentence+=word.rsplit('/',1)[0]+' '
            classes.add(word.rsplit('/',1)[1])
        sentence+='%%%END%%%'
        lines.append(sentence)
    classlist=list(classes)
    train(classlist,lines)
    

def updateweights(context,actualclass):
        predictedclass={}
        for i in range(len(classlist)):
            predictedclass[classlist[i]]=0
        for i in range(len(classlist)):
            for word in context:
                try:
                    predictedclass[classlist[i]]+=feature[word]*weight[classlist[i]][word]
                except:
                    predictedclass[classlist[i]]+=0
        argmax=classlist[0]
        for key in predictedclass:
            if predictedclass[key]>predictedclass[argmax]:
                argmax=key
        if argmax!=actualclass:
            for word in context:
                weight[argmax][word]-=feature[word]
                weight[actualclass][word]+=feature[word]
    
def train(classlist_passed,lines):
    N=25
    global weight,weightavg
    global classlist
    classlist=classlist_passed
    weight={}
    weightavg={}
    for eachclass in classlist:
        weight[eachclass]={}
        weightavg[eachclass]={}
    for x in range(N):
        for line in random.sample(lines,len(lines)):
            words=line.split()
            for index in range(2,len(words)-1,2):
                global feature
                feature={}
                try:
                    posp=words[index-2].rsplit('/',1)[1]
                except:
                    posp=''
                posc=words[index].rsplit('/',1)[1]
                try:
                    posn=words[index+2].rsplit('/',1)[1]
                except:
                    posn=''
                
                wprev='w_prev'+words[index-2].rsplit('/',1)[0]
                wcurr='w_curr'+words[index].rsplit('/',1)[0]
                try:
                    wnext='w_next'+words[index+2].rsplit('/',1)[0]
                except:
                    wnext='w_next'+words[index+1].rsplit('/',1)[0]
                
                try:
                    prev_entity=words[index-3]
                except:
                    prev_entity='%%not_defined%%'
                
                context=[wprev,wcurr,wnext,posp,posc,posn,prev_entity]
                for eachword in context:
                    feature[eachword]=1
                for eachclass in classlist:
                    for eachword in context:
                        if eachword not in weight[eachclass]:
                            weight[eachclass][eachword]=0
                updateweights(context,words[index-1])
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


build()                
    

    
