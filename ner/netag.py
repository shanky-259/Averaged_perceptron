import sys
import json
files=sys.argv
import codecs
sys.stdin = codecs.getreader('latin-1')(sys.stdin.detach())

    
def loadmodell():
    f=open(str(files[1]),'r')
    weightavg=json.loads(f.read())
    return weightavg

def classify(classlist):
    for eachline in sys.stdin.readlines():
        wordss=eachline.split()
        line='%%%BEGIN%%%'+' '
        for word in wordss:
            line+=word+' '
        line+='%%%END%%%'
        percepclassify(line,classlist,weightavg)
        
def percepclassify(line,classlist,weightavg):
    output=''
    words=line.split()
    maximum='%%not_defined%%'
    for index in range(1,len(words)-1):
        try:
            posp=words[index-1].split('/')[1]
        except:
            posp=''
        posc=words[index].split('/')[1]
        try:
            posn=words[index+1].split('/')[1]
        except:
            posn=''
        wprev='w_prev'+words[index-1].split('/')[0]
        wcurr='w_curr'+words[index].split('/')[0]
        wnext='w_next'+words[index+1].split('/')[0]
        prev_entity=maximum
        classifydev={}
        feature={}
        context=[wprev,wcurr,wnext,posp,posc,posn,prev_entity]
        for eachword in context:
            feature[eachword]=1
        for eachclass in classlist:
            classifydev[eachclass]=0
        for eachclass in classlist:
            for eachword in context:
                try:
                    classifydev[eachclass]+=feature[eachword]*weightavg[eachclass][eachword]
                except:
                    classifydev[eachclass]+=0
        maximum=classlist[0]
        for eachclass in classlist:
            if classifydev[eachclass]>classifydev[maximum]:
                maximum=eachclass
        output+=words[index]+'/'+maximum+' '
    print(output)
            

weightavg=loadmodell()
classlist=[]
for key in weightavg:
    classlist.append(key)
classify(classlist)
