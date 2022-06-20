"""
Takes a target and array of numbers and returns the shortest set of numbers that
give the desired sum.
"""


def bestSum(target: int, nums: list) -> list:
    '''    
    Brute Force
    time: O(n^m*m)
    space: O(m^2)

    Parameters
    ----------
    target : int  
        the desired sum
    nums : list[int]  
        the provided array of numbers.

    Returns
    -------
    list : 
        the set of numbers with sum as required.
    '''
    if target == 0:
        return []
    if target < 0:
        return None

    m = None
    for num in nums:
        r = bestSum(target-num, nums)
        if r != None:
            r.append(num)
            if m == None or len(r) < len(m):
                m = r

    return m


def bestSum_memoized(target: int, nums: list, memo={}) -> list:
    """
    Memoized solution
    time: O(n*m)
    """
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    smallest = None
    for num in nums:
        r = bestSum_memoized(target-num, nums, memo)
        if r != None:
            r = r[:]
            r.append(num)
            if smallest == None or len(r) < len(smallest):
                smallest = r

    memo[target] = smallest
    return memo[target]


def bestSum_tab(target, nums):
    '''
        Tabulation Method
        O(n*m^2) time
        O(m^2) space
    '''
    table = [None]*(target+1)
    table[0] = []
    for i in range(target+1):
        if table[i] == None:
            continue

        for num in nums:
            if i+num <= target:
                new_v = table[i][:]
                new_v.append(num)
                if not table[i+num] or len(table[i+num]) > len(new_v):
                    table[i+num] = new_v

    return table[target]


print(bestSum(8, [2, 3, 5]))  # [5,3]
print(bestSum(7, [3, 4, 5, 7]))  # [7]
print(bestSum(8, [1, 4, 5]))  # [4,4]
# print(bestSum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
print(bestSum_memoized(8, [2, 3, 5], {}))  # [5, 3]
print(bestSum_tab(7, [3, 4, 5, 7]))  # [7]
print(bestSum_tab(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
print(bestSum_tab(300, [1, 7, 14, 21]))
# [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 1, 1, 1, 1, 1, 1]
