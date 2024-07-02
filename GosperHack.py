"""
int state = (1 << k) - 1;            
while (state < (1 << m))
{
    doSomething(state);

    int c = state & - state;
    int r = state + c;
    state = (((r ^ state) >> 2) / c) | r;
}

"""
"""
https://read.seas.harvard.edu/~kohler/class/cs207-s12/lec12.html
"""

#Given N elements, traverse subsets of size K (Gosper's Hack)

k = 2
m = 3
state = (1<<k) -1
limit = (1<<m)
while(state<limit):
    #doSomething(state)
    c = state & (-state)                # determine rightmost 1 bit
    r = state + c                       # determine carry bit
    state = int(((state^r)>>2)/c) | r   # produce block of ones that begins at the least-significant bit


def subsets_eq_k(A,K):
    subsets = []
    N = len(A)

    # iterate over subsets of size K
    state = (1<<K)-1     # 2^K - 1 is always a number having exactly K 1 bits
    while state < (1<<N):
        subset = []
        for n in range(N):
            if ((state>>n)&1) == 1:
                subset.append(A[n])
 
        subsets.append(subset)
 
        # catch special case
        if state == 0:
            break
 
        c = state & (-state)                # determine rightmost 1 bit
        r = state + c                       # determine carry bit
        state = int(((state^r)>>2)/c) | r   # produce block of ones that begins at the least-significant bit


    return subsets
 
if __name__ == '__main__':
    A = [4,5,7,9]
    K = 2

    # print subsets
    for subset in subsets_eq_k(A,K):
        print(subset)
