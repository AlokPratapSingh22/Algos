"""
howSum(targetSum, numbers) - takes a list of nums and a target sum as input and returns the possible set of numbers that result in target sum.
"""


def howSum(target: int, nums: list) -> list:
    '''
    returns the set of numbers in nums list that can produce the target sum.  

    BRUTE FORCE METHOD    
    Complexity: n = len(nums), m = target  
    O(n^m * m) time and 
    O(m+m) space

    Parameters
    ----------
    target : int
        required target sum

    nums : list
        provided list of non-negative numbers

    Returns
    -------
    list
        list of numbers that form target sum

    '''

    if target == 0:
        return []

    if target < min(nums):
        return None
    ans = []
    for num in nums:
        r = howSum(target-num, nums)
        if r != None:
            r.append(num)
            return r

    return None


def howSum_memoized(target: int, nums: list, memo={}) -> list:
    '''
    returns the set of numbers in nums list that can produce the target sum.  

    MEMOIZATION METHOD    
    Complexity: n = len(nums), m = target  
    O(n*m^2) time and 
    O(m^2) space

    Parameters
    ----------
    target : int
        required target sum

    nums : list
        provided list of non-negative numbers


    Returns
    -------
    list
        list of numbers that form target sum

    '''
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for num in nums:
        r = howSum_memoized(target-num, nums, memo)
        if r != None:
            r.append(num)
            memo[target] = r
            return r

    memo[target] = None
    return None

def howSum_tab(target:int, nums:list[int]) -> list :
    '''
        returns the set of numbers in nums list that can produce the target sum.  

        MEMOIZATION METHOD    
        Complexity: n = len(nums), m = target  
        O(n*m^2) time and 
        O(m^2) space

        Parameters
        ----------
        target : int
            required target sum

        nums : list
            provided list of non-negative numbers


        Returns
        -------
        list
            list of numbers that form target sum

    '''

    table = [None for _ in range(target+1)]
    table[0] = []

    for i in range(target+1):
        if table[i] == None: continue    
        for num in nums:
            if i+num <= target:                
                table[i+num] = table[i].copy()
                table[i+num].append(num)

    return table[target]


print(howSum(7, [2, 4]))  # None
print(howSum(7, [5, 3, 4, 7]))  # [4,3]
print(howSum_tab(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(howSum_tab(300, [7, 14]))  # None
print(howSum_tab(300, [7, 20, 14]))  # [20, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]