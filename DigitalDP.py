"""
LC 2376. Count Special Integers
We call a positive integer special if all of its digits are distinct. 
Given a positive integer n, return the number of special integers that belong to the interval [1, n].

Example 1:
Input: n = 20
Output: 19
Explanation: All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers.

Example 2:
Input: n = 5
Output: 5
Explanation: All the integers from 1 to 5 are special.

Example 3:
Input: n = 135
Output: 110
Explanation: There are 110 integers from 1 to 135 that are special.
Some of the integers that are not special are: 22, 114, and 131.


Constraints:

    1 <= n <= 2 * 109

"""
"""
Sample questions: 
LC 2376, 2719,1067, 233, 902, 357, 1067, 2801,

"""

    def countSpecialNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        inputList = list(str(n))
        inputList = list(map(int,inputList))        
        self.memo = {}
        ans = self.digitalDP(0,0,True,False,inputList)
        return ans

    def digitalDP(self,idx,mask,isPrefix,isLeadingZero,inputList):
        #inputList: '2345'
        #idx: current digit pos in inputList (from left, 0 indexed)
        #mask: all numbers have been used before
        #isPrefix: all previous numbers are prefix of inputList. 
        #For instance, 23_ (isPrefix True). Then the third digit can only go to 4. 
        #If isPrefix False, then the third digit can go to 9.
        #isLeadingZero: Is valid number showing up in mask. Is there any leading zero.
        #False: no. We have two options.
        #Option 1: we could skip current digit and go to next digit. 
        #Option 2: don't skip. Then we could only start from 1
        #True:yes. Then we cannot skipp current digit. At current digit, we could start from 0.
        n = len(inputList)
        key = (idx,mask,isPrefix,isLeadingZero)

        if(idx == n): 
            self.memo[key] = int(isLeadingZero)
            return self.memo[key]

        if(key in self.memo):
            return self.memo[key]
        
        ans = 0
        if(not isLeadingZero):
            ans += self.digitalDP(idx+1,mask,False,False,inputList)

        #Determin the up limit of our target digits.
        if(isPrefix):
            #we are on the prefix of inputlist. We could only go up to inputList[idx]
            up = inputList[idx]
        else:
            # we are not on the prefix. So we could go up to 9
            up = 9

        if(isLeadingZero):
            #Valid number showing up in mask.We could go start from 0. 
            low = 0
        else:
            #Valid number not showing up in mask.We could only go start from 1. 
            low = 1

        targetList = range(low,up+1)

        for digit in targetList:
            if(mask>>digit&1):
                continue

            nextIsPrefix = (isPrefix and digit==up)
            ans += self.digitalDP(idx+1,mask|1<<digit,nextIsPrefix,True,inputList)
                    
        self.memo[key] = ans

        return self.memo[key]
