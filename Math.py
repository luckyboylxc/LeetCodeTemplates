#Test

MOD = 10**9 + 7

def gcd(x,y):
    if(y == 0):
        return x
    return gcd(y,x%y)

#compute combinations
up = 10**4+15
c = [[1 for k in range(15)] for n in range(up)] #c[n][k]
MOD = 10**9 + 7
for n in range(1,up):
    for k in range(1,15):
        c[n][k] = n*c[n-1][k-1]//k

M = 10**4+1
def computespf(n):
    spf = [i for i in range(n)]
    for i in range(2,n):
        if(spf[i]<i):
            continue
        for j in range(i*i,n,i):
            spf[j] = i
    
    return spf

def inv(x):
    return quickPow(x, MOD - 2,MOD)

def fast_power(base, power, MOD):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0

    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """

    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % MOD

    return result

def quickPow(x,y,m):
    if(y==0):
        return 1
    
    p = quickPow(x,y//2,m)%m
    p = (p*p)%m
    if(y%2 == 1):
        p = p*x%m
    return p

def linearInverse(n):
    invList = [1 for i in range(n+1)]
    for i in range(2,n+1):
        invList[i] = (MOD - MOD//i) * invList[MOD%i]%MOD
    
    return invList

def linearInverseForInputArray(nums):
    #Cualculate the inverse of any n nums in nums List in a linear way
    n = len(nums)
    prodList = [0 for i in range(n+1)]
    prodList[0] = 1
    for i in range(1,n+1):
        prodList[i] = prodList[i-1] * nums[i-1]%MOD
    
    prodInverseList = [0 for i in range(n+1)]

    prodInverseList[n] = quickPow(prodInverseList[n],MOD-2,MOD)
    for i in range(n,0,-1):
        prodInverseList[i-1] = prodInverseList[i] * nums[i-1]%MOD

    invList = [0 for i in range(n)]
    for i in range(n):
        invList[i] = prodInverseList[i+1]*prodList[i]%MOD

    return invList
