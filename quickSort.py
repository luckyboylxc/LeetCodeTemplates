import random
def quickSort(nums,l,r):
    if(l>=r):
        return
    pIdx = getPivot(nums,l,r)
    quickSort(nums,l,pIdx)
    quickSort(nums,pIdx+1,r)

def getPivot(nums,lt,rt):
    ''' This function takes first element as pivot, and places
      all the elements smaller than the pivot on the left side
      and all the elements greater than the pivot on
      the right side. It returns the index of the last element
      on the smaller side '''
    
    left = lt
    right = rt
    #pivotIdx = (lt+rt)//2
    pivotIdx = random.randint(lt,rt)
    nums[lt],nums[pivotIdx] = nums[pivotIdx],nums[lt]
    pivot = nums[lt]

    left -=1
    right +=1
    while(True):
        left +=1
        right -= 1

        while(nums[left] < pivot):
            left +=1
        
        while(nums[right] > pivot):
            right -=1
        
        if(left >= right):
            return right

        nums[left],nums[right] = nums[right], nums[left]

tempList = [3,3,3,1,1,1,4,5,6]
quickSort(tempList,0,8)
print(tempList)