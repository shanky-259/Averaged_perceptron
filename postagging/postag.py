import sys
import json
import random
files=sys.argv
'''postagnew also checks the accuracy of the entire document TESTPOSFILE by checking the correctness of each word
which is not done in postag.py  but uses prev curr and next words as features not done in postagfull'''
class postag:
    def __init__(self):
        pass
    
    def loadmodell(self):
        f=open(str(files[1]),'r')
        weightavg=json.loads(f.read())
        return weightavg
    
    def classifyex(self):
        lines=input()
        output=''
        wordss=lines.split()
        line='%%%BEGIN%%%'+' '
        for word in wordss:
            line+=word+' '
        line+='%%%END%%%'
        words=line.split()
        for index in range(1,len(words)-1):
            wprev='w_prev'+words[index-1]
            wcurr='w_curr'+words[index]
            wnext='w_next'+words[index+1]
            classifydev={}
            feature={}
            for i in range(len(classlist)):
                feature[classlist[i]]={}
            relative=[wprev,wcurr,wnext]
            for eachword in relative:
                for i in range(len(classlist)):
                    feature[classlist[i]][eachword]=1
            '''for each word sum up the dot product of feature and weighted avg,result will be the class with max value'''
            for eachclass in classlist:
                classifydev[eachclass]=0
            for eachclass in classlist:
                for eachword in relative:
                    try:
                        classifydev[eachclass]+=feature[eachclass][eachword]*weightavg[eachclass][eachword]
                    except:
                        classifydev[eachclass]+=0
            maximum=classlist[0]
            for eachclass in classlist:
                if classifydev[eachclass]>classifydev[maximum]:
                    maximum=eachclass
            output+=words[index]+'/'+maximum+' '
        print(output+"\n")
                
if __name__ == '__main__':
    s=postag()
    weightavg=s.loadmodell()
    classlist=[]
    for key in weightavg:
        classlist.append(key)
    s.classifyex()