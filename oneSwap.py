# def can_be_non_decreasing_after_one_swap(A):
#     out_of_order_count = 0
#     n = len(A)

#     for i in range(1, n):
#         if A[i] < A[i-1]:
#             out_of_order_count += 1
#             if out_of_order_count > 1:
#                 return False
#             if i == 1 or A[i-2] <= A[i]:
#                 continue
#             elif i == n - 1 or A[i-1] <= A[i+1]:
#                 continue
#             else:
#                 return False
    
#     return True

"""
A non-empty zero-indexed array A consisting of N integers is given. You can performance 1 or less swap operation in array A. The goal is to check whether array A can be non-decreasing order after 1 or less swap.

Example 1: [1,5,8,3] => False
Example 2: [1,2,3,5,4] => True
Example 3: [1,5,3,4,2] => True
Example 4: [1,5,2,3,4] => False
Example 5: [3,2,1] => True

"""
def canSwap_Wrong(A):
    out_of_order_count = 0
    n = len(A)

    for i in range(1, n):
        if A[i] < A[i-1]:
            out_of_order_count += 1
            if out_of_order_count > 1:
                return False
            if i == 1 or A[i-2] <= A[i]:
                continue
            elif i == n - 1 or A[i-1] <= A[i+1]:
                continue
            else:
                return False
    
    return True

def canSwap(nums):
    if len(nums) <= 2:
        return True
    
    n = len(nums)
    first, second = -1, -1
    
    for i in range(n-1):
        if nums[i] <= nums[i+1]:
            continue
        else:
            if first == -1:
                first, second = i, i+1
            elif first+ 1 == second:
                second = i+1
            else:
                return False
    
    return ((first == 0 or nums[first-1] <= nums[second]) and nums[second] <= nums[first+1]) \
            and (nums[second-1] <= nums[first] and (second == n-1 or nums[first] <= nums[second+1]))



# Test cases
print(canSwap([1, 5, 8, 3]))   # Output: False
print(canSwap([1, 2, 3, 5, 4])) # Output: True
print(canSwap([1, 5, 3, 4, 2])) # Output: True
print(canSwap([1, 5, 2, 3, 4])) # Output: False
print(canSwap([3, 2, 1]))      # Output: True
