def ternary_search(f, left, right, absolute_precision) -> float:
    """Find maximum of unimodal function f() within [left, right].
    To find the minimum, reverse the if/else statement or reverse the comparison.
    """
    while abs(right - left) >= absolute_precision:
        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3

        if f(left_third) < f(right_third):
            left = left_third
        else:
            right = right_third

     # Left and right are the current bounds; the maximum is between them
    return (left + right) / 2

def ternary_search_max(f, left, right) -> int:
    """Find maximum of unimodal function f() within [left, right].
    To find the minimum, reverse the if/else statement or reverse the comparison.
    """
    while (right - left) >= 3:
        mid1 = left + (right - left) //3
        mid2 = right - (right - left) //3

        if f(mid1) < f(mid2):
            left = mid1
        elif(f(mid1) > f(mid2)):
            right = mid2
        else:
            left = mid1
            right = mid2

    # Left and right are the current bounds; the maximum is between them
    # check all idx between left and right (inclusive)
    res = float('-inf')
    for idx in range(left,right+1):
        res = max(res,f(idx))
    return res

def ternary_search_min(f, left, right) -> int:
    """Find mind value of unimodal function f() within [left, right].
    """
    while (right - left) >= 3:
        mid1 = left + (right - left) //3
        mid2 = right - (right - left) //3

        if f(mid1) > f(mid2):
            left = mid1
        elif(f(mid1) < f(mid2)):
            right = mid2
        else:
            left = mid1
            right = mid2

    # Left and right are the current bounds; the maximum is between them
    # check all idx between left and right (inclusive)
    res = float('inf')
    for idx in range(left,right+1):
        res = min(res,f(idx))
    return res