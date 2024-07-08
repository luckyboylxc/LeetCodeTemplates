#Find all prime numbers <=num
def prime_eratosthenes(num):
    #Time Complexity: O(n*log(log(n)))
    #Space Complexity: O(n)

    primeList = []
    isPrime = [True for i in range(num+1)]
    isPrime[0] = isPrime[1] = False
    for i in range(2,int(num**0.5)+1):
        if(isPrime[i]):
            for j in range(i*i,num+1,i):
                isPrime[j] = False
                
    for i in range(2, num+1):
        if isPrime[i]:
            primeList.append(i)
    
    return primeList

# calculate distinct prime factors 
maxNum = 10**5 
isPrime = [True] * (maxNum+1)
isPrime[0] = isPrime[1] = False
count = [0]* (maxNum+1)
for i in range(2,maxNum+1):
    if(isPrime[i]):
        for j in range(i,maxNum+1,i):
            count[j] +=1

def sieve(n):
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    #return: smallest prime factors
    spf = [i for i in range(n+1)]
    for i in range(2,int(n**0.5)+2):
        if(spf[i] != i):
            continue
        for k in range(i*i,n+1,i):
            if(spf[k]>i):
                spf[k] = i
    return spf


def prime_linear(n):
    #Time Complexity: O(n)
    #Space Complexity: O(n)

    spf = [0] * (n+1) #smallest prime factor
    primeList = []

    for i in range(2,n+1):
        if(spf[i]==0):
            spf[i] = i
            primeList.append(i)
        for j in range(len(primeList)):
            if(i * primeList[j]>n):
                break
            if(primeList[j]>spf[i]):
                break
            spf[i*primeList[j]] = primeList[j]
        
    return spf

#get all prime factor list using spf (smallest prime factor)
#For instance, for x=100, you'll get [2,2,5,5]
def prime_factors(x,spf):
    res = []
    while(spf[x]>1):
        res.append(spf[x])
        x //= spf[x]
    return res

#compute prime factors (including duplicate) number using spf (smallest prime factor)
#For instance, for x=100, the prime factor list is [2,2,5,5]. You'll get 4
def countDuplicatePrimeFactors(x,spf):
    count = 0
    while(spf[x]>1):
        count+=1
        x //= spf[x]
    return count

#get min and max prime factor for all numbers not greater than n
def get_minAndmaxPrimeFactor(n):
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    maxFactorList = [0] * (n+1) #largest prime factor
    minFactorList = [0] * (n+1) #smallest prime factor
    primeList = []

    for i in range(2,n+1):
        if(minFactorList[i]==0):
            minFactorList[i] = i
            primeList.append(i)
        for j in range(len(primeList)):
            if(i * primeList[j]>n):
                break
            if(primeList[j]>minFactorList[i]):
                break
            minFactorList[i*primeList[j]] = primeList[j]
    
    maxFactorList[1] = 1
    for i in range(2,n+1):
        maxFactorList[i] = max(minFactorList[i],maxFactorList[i//minFactorList[i]])

    return minFactorList,maxFactorList


    # Print all prime numbers
    # count = 0
    # for i in range(2, num+1):
    #     if isPrime[i]:
    #         count +=1
    # print("There are {0} prime numbers with upper bound of {1}".format(count,num))




# Driver code
if __name__ == '__main__':
    n = 10**5
    pl1 = prime_eratosthenes(n)
    print(pl1)

    spf = prime_linear(n)
    
    minList,maxList = get_minAndmaxPrimeFactor(n)
    equalFlag = True
    for i in range(2,n+1):
        primeList = prime_factors(i,spf)
        count = countDuplicatePrimeFactors(i,spf)
        primeList.sort()
        if(i==1000):
            print(primeList)
            print(count)

        if(minList[i] != primeList[0]):
            print("Min prime factor for {0} is not {1}".format(i,minList[i]))
            equalFlag = False
        
        if(maxList[i] != primeList[-1]):
            print("Max prime factor for {0} is not {1}".format(i,maxList[i]))
            equalFlag = False
    if(equalFlag):
        print("All min and max factors for numbers <= {0} are equal".format(n))
    else:
        print("Sth is wrong")