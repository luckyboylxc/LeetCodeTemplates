import bisect

# We want a maximum function which accepts a default value
from functools import partial, reduce

def patience_sort_longestLenth(xs):
    '''Patience sort an iterable, xs.

    This function generates a series of pairs (x, pile), where "pile"
    is the 0-based index of the pile "x" should be placed on top of.
    Elements of "xs" must be less-than comparable.
    '''
    pile_tops = list()
    for x in xs:
        pileID = bisect.bisect_left(pile_tops, x)
        if pileID == len(pile_tops):
            pile_tops.append(x)
        else:
            pile_tops[pileID] = x
        
    return len(pile_tops)


def patience_sort(xs):
    '''Patience sort an iterable, xs.

    This function generates a series of pairs (x, pile), where "pile"
    is the 0-based index of the pile "x" should be placed on top of.
    Elements of "xs" must be less-than comparable.
    '''
    pile_tops = list()
    for x in xs:
        pileID = bisect.bisect_left(pile_tops, x)
        if pileID == len(pile_tops):
            pile_tops.append(x)
        else:
            pile_tops[pileID] = x
        yield x, pileID

def longest_increasing_subseq_length(xs):
    '''Return the length of the longest increasing subsequence of xs.

    >>> longest_increasing_subseq_length(range(3))
    3
    >>> longest_increasing_subseq_length([3, 1, 2, 0])
    2
    '''
    ans = 0
    for x,pileID in patience_sort(xs):
        ans = max(ans,pileID+1)
    return ans

def longest_increasing_subsequence(xs):
    '''Return a longest increasing subsequence of xs.

    (Note that there may be more than one such subsequence.)
    >>> longest_increasing_subsequence(range(3))
    [0, 1, 2]
    >>> longest_increasing_subsequence([3, 1, 2, 0])
    [1, 2]
    '''
    # Patience sort xs, stacking (x, prev_ix) pairs on the piles.
    # Prev_ix indexes the element at the top of the previous pile,
    # which has a lower x value than the current x value.
    piles = [[]] # Create a dummy pile 0
    for x, pileID in patience_sort(xs):
        #print("Num:{0}, Pos:{1}".format(x,pileID))
        if pileID + 1 == len(piles):
            #print("Add [] to piles")
            piles.append([])
        # backlink to the top of the previous pile
        piles[pileID + 1].append((x, len(piles[pileID]) - 1)) 
        # Backtrack to find a longest increasing subsequence
        #print(piles)

    npiles = len(piles) - 1
    prev = 0
    lis = []
    for pile in range(npiles, 0, -1):
        x, prev = piles[pile][prev]
        lis.append(x)
    lis.reverse()
    return lis

res = longest_increasing_subseq_length([3, 1, 2, 0])
print("Longest increasing Subseq Len:{0}".format(res))

tempList = longest_increasing_subsequence([3, 1, 2, 0])
print("Longest increasing Subseq List:{0}".format(tempList))