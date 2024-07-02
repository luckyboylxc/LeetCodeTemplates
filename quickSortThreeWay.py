import random
def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        T = n - k + 1
        def getPivotIdx(left,right):
            rIdx = random.randint(left,right)
            nums[left],nums[rIdx] = nums[rIdx],nums[left]

            lt = left  # left most pos that's equal to pivot
            rt = right # right most pos that's equal to pivot
            t = left # current pos in 
            pivot = nums[left]
            while(t<= rt):
                if(nums[t]<pivot):
                    nums[t],nums[lt] = nums[lt],nums[t]
                    t +=1
                    lt +=1
                elif(nums[t]>pivot):
                    nums[t],nums[rt] = nums[rt],nums[t]
                    rt -=1
                else:
                    t +=1
            
            return (lt,rt)
        
        def quickSelect(left,right,target):
            i,j = getPivotIdx(left,right)
            pivot = nums[i]
            if(i-left>= target):
                return quickSelect(left,i-1,target)
            elif(j-left+1>= target):
                return pivot
            else:
                return quickSelect(j+1,right,target-(j-left+1))
        
        return quickSelect(0,n-1,T)

def partition3(A, l, r):
    """
    partition3: A partition for quicksort algorithm. We'll use the 3-way to handle few equal elements in array (happens
    a lot in practical use.)
    This function is called from the main function quick_sort.
    RETURNS: leftMost and rightMost postion of the pivot num
    """
    #lt: the left most position equal to pivot num
    #gt: the right most position equal to pivot num
    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l   # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = A[l]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= gt:      # Starting from the first element.
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
    print("Left Most:{0},Right Most:{1}".format(lt,gt))
    return lt, gt



def quick_sort(A, l, r):
    """
    quick_sort: One of the most used sorting algorithm. 
    It makes to recursive calls. One to sort the left part separately, other for sorting the right part.
    The partition key is chosen randomly via ``random.randint(l, r)`` and it's between the ``l,  r``.
    
    PARAMETERS:
    -----------
    A: Array or the sequence that we want to sort.
    l: The lower bound of the array that we want to sort. It's not very important we might replace it by a wrapper function
    that only takes in an array as input. In this case it's the first element in the left part of the array.
    r: It's the same as l, only differs as it's the first element from the end.
    
    RETURNS:
    -------
    Sorted list A.
    """
    if l >= r: 
        return
    
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]
    print('Pivot Num:{0}'.format(A[l]))
    
    lt, gt = partition3(A, l, r)
    quick_sort(A, l, lt - 1)
    quick_sort(A, gt + 1, r)  

tempList = [3,3,3,1,1,1,4,5,6]
quick_sort(tempList,0,8)
print(tempList)