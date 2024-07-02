
def KMPSearch_Old(pat, txt):
    M = len(pat)
    N = len(txt)    
    # create lps[] that will hold the longest prefix suffix
    # Preprocess the pattern (calculate lps[] array)
    lps = calculateLPS_OLD(pat)
    
    j = 0 # index for pat[]
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
            if j == M:
                print ("Found pattern at index", str(i-j))
                j = lps[j-1] 
        # mismatch after j matches
        else:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
def calculateLPS_OLD(pat):    
    M = len(pat)
    lps = [0] * M
    # lps[0] is always 0
    lps[0] = 0 
    i = 1
    currLen = 0 # length of the previous longest prefix suffix
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[currLen]:
            currLen += 1
            lps[i] = currLen
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if currLen != 0:
                currLen = lps[currLen-1] 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    
    return lps

def calculateLPS(pat):
    #https://github.com/wisdompeak/LeetCode/tree/master/String/1392.Longest-Happy-Prefix
    M = len(pat)
    dp = [0] * M
    # lps[0] is always 0
    dp[0] = 0
    for i in range(1,M):
        j = dp[i-1]
        while(j>=1 and pat[j]!=pat[i]):
            j = dp[j-1]
        dp[i] = j + (pat[j] == pat[i])        
    return dp

def KMPSearch(self, pat, txt):
        M = len(pat)
        N = len(txt)    
        # create lps[] that will hold the longest prefix suffix
        # Preprocess the pattern (calculate lps[] array)
        
        #resList: all starting index that pat showing up in txt
        resList = []

        lps = self.calculateLPS(pat)
        dp = [0]*N
        dp[0] = (pat[0] == txt[0])
        if(dp[0] == M):
            resList.append(0-M+1)
        for i in range(1,N):
            j = dp[i-1]
            while((j>0 and j<M and txt[i] != pat[j]) or (j==M)):
                j = lps[j-1]
            dp[i] = j + (txt[i] == pat[j])
            if(dp[i] == M):
                resList.append(i-M+1)

        return resList        

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)    
    # create lps[] that will hold the longest prefix suffix
    # Preprocess the pattern (calculate lps[] array)
    lps = calculateLPS(pat)
    
    dp =[0]*N
    if(pat[0] == txt[0]):
        dp[0] = 1
    if(dp[0] == M):
        print ("Found pattern at index", str(0-M+1))
    
    for i in range(1,N):        
        j = dp[i-1]
        while(((j>0 and j<M) and txt[i] != pat[j]) or (j==M)):
            j = lps[j-1]
        dp[i] = j + (txt[i] == pat[j])
        if(dp[i] == M):
            print ("Found pattern at index", str(i-M+1))
        



def main():
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    KMPSearch(pattern,text)
    return 0

if __name__ == "__main__":
    main()
