
def percepclassify(line,classlist,weightavg):
    output=''
    words=line.split()
    for index in range(1,len(words)-1):
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
    
    
