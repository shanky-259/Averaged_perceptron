import sys
import json
files=sys.argv
sys.stdin = codecs.getreader('latin-1')


def loadmodell():
    f=open(str(files[1]),'r',encoding='latin-1')
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
    for index in range(1,len(words)-1):
        flag='false'
        for i,each in enumerate(regex):
            if re.findall(regex[i][0],words[index])==[words[index]]:
                maximum=regex[i][1]
                flag='true'
                
        if flag=='true':
            continue
        else:
            wprev='w_prev'+words[index-1]
            wcurr='w_curr'+words[index]
            wnext='w_next'+words[index+1]
            classifydev={}
            feature={}
            context=[wprev,wcurr,wnext]
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
regex=[(r'.*ing$','VBG'),(r'.*ed$','VBD'),(r'.*es$','VBZ'),(r'.*\'s$','NN$'),(r'.*s$','NNS')]
classify(classlist)
    

