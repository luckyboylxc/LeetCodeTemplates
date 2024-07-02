import collections
def predictPartyVictory( senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        inputList = list(senate)
        freMap = collections.Counter(inputList)
        
        resMap = {'R':'Dire', 'D':'Radiant'}

        if(freMap['D'] == 0):
            return resMap['D']
        
        if(freMap['R'] == 0):
            return resMap['R']
        
        vote = True
        count = 0
        queueMap = collections.defaultdict(list)
        oppMap = {'R':'D','D':'R'}
        block = [False] * (len(inputList))

        remainMap = {}
        remainMap['R'] = freMap['R']
        remainMap['D'] = freMap['D']

        while(vote):
            for i in range(len(inputList)):
                curr =  inputList[i]
                remainMap[curr] -=1

                if(count == 0):
                    anchor = curr
                    queueMap[anchor].append((anchor,i))
                    opp = oppMap[anchor]
                
                    if(remainMap[opp]>0 or len(queueMap[opp]) == 0):
                        count +=1
                    else:
                        ch,idx = queueMap[opp].pop(0)

                        freMap[ch] -=1
                        #remainMap[ch] -=1
                        block[idx] = True
                        if(freMap[ch] == 0):
                            return resMap[opp]
                else:
                    if(anchor == curr):
                        queueMap[curr].append((curr,i))
                        opp = oppMap[curr]

                        if(remainMap[opp]>0 or len(queueMap[opp]) == 0):
                            count +=1
                        else:
                            ch,idx = queueMap[opp].pop(0)                            
                            freMap[opp] -=1
                            block[idx] = True
                            #remainMap[opp] -=1
                            if(freMap[opp] == 0):
                                return resMap[opp]
                            
                    else:
                        count -=1
                        freMap[curr] -=1
                        block[i] = True
                        if(freMap[curr] == 0):
                            return resMap[curr]
                # print('Idx:{0}.Count:{1},Anchor:{2}'.format(i,count,anchor))
                # print(block)
                # print('R:{0}, Remain count:{1}'.format(queueMap['R'],remainMap['R']))
                # print('D:{0}, Remain count:{1}'.format(queueMap['D'],remainMap['D']))
                # print(block)
            while(count>0):
                opp = oppMap[anchor]
                ch,idx = queueMap[opp].pop(0)                            
                freMap[opp] -=1
                block[idx] = True
                #remainMap[opp] -=1
                if(freMap[opp] == 0):
                    return resMap[opp]
                count -=1
                
                        
            tempList = []
            for i in range(len(inputList)):
                if(not block[i] ):
                    tempList.append(inputList[i])
            inputList = list(tempList)
            print(inputList)
            count = 0
            queueMap = collections.defaultdict(list)
            block = [False] * (len(inputList))
            freMap = collections.Counter(inputList)
            remainMap = {}
            remainMap['R'] = freMap['R']
            remainMap['D'] = freMap['D']


if __name__ == '__main__':
    senate = "DDDRDRRDRRDRDRRRDDRRDDDRDRDDDRRRRDDDDRDRRRRDRRRDRDRDDRDRRRRDRDRRRDRDDDRRDDDRDRDRDRRDRDDRDDRDDDDRDRRR"
    res = predictPartyVictory(senate)
    print("Winner is {0}".format(res))
