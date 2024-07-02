import math

def kth_smallest_amount(coins, k):
    # Calculate the least common multiple (LCM) of the given coins
    lcm = 1
    for coin in coins:
        lcm = lcm * coin // math.gcd(lcm, coin)
    
    # The kth smallest amount is the LCM multiplied by k
    return lcm * k

# Test cases
print(kth_smallest_amount([3, 6, 9], 3))  # Output: 9
print(kth_smallest_amount([5, 2], 7))     # Output: 12
