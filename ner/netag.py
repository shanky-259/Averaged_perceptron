import sys
import json
import random
files=sys.argv
'''postagnew also checks the accuracy of the entire document TESTPOSFILE by checking the correctness of each word
which is not done in postag.py  but uses prev curr and next words as features not done in postagfull'''
class neclassify:
    def __init__(self):
        pass
    
    def loadmodell(self):
        f=open(str(files[1]),'r')
        weightavg=json.loads(f.read())
        return weightavg
    
    def classifyex(self):
        k=0
        total=0
        for lines in open(files[2],'r'):
            wordss=lines.split()
            line='%%%BEGIN%%%'+' '
            for word in wordss:
                line+=word.rsplit('/',1)[1]+' '
                line+=word.rsplit('/',1)[0]+' '
            line+='%%%END%%%'
            words=line.split()
            for eachword in words:
                if word not in ('%%%BEGIN%%%','%%%END%%%'):
                    total+=1
            for index in range(2,len(words)-1,2):
                wprev='w_prev'+words[index-2]
                wcurr='w_curr'+words[index]
                try:
                    wnext='w_next'+words[index+2]
                except:
                    wnext='w_next'+words[index+1]
                actualclass=words[index-1]
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
                if maximum!=actualclass:
                    k+=1
        print("the total accuracy is : %s"%(1-(k/total)))
            
if __name__ == '__main__':
    s=neclassify()
    weightavg=s.loadmodell()
    classlist=[]
    for key in weightavg:
        classlist.append(key)
    s.classifyex()