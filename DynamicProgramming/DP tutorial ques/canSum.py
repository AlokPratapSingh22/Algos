"""
canSum(targetSum, numbers) - find whether the targetSum can be achieved using the numbers in numbers array.
You can use a number any no. of times
Numbers array contains non-negative numbers

"""
def canSum(target: int, nums: list[int]) -> bool:
    ''' 
    returns whether target can be achieved using numbers in nums array
    
    Brute force method -
        Complexity: O(n^m) time and O(m) space

    Parameters
    ----------
    target : int
        The target sum in question
    nums : list[int]
        The list of non-negative integers provided

    Returns
    -------        
    bool
        true or false (i.e. possible or not) 

    '''
    if target == 0:
        return True

    if target < 0:
        return False

    for num in nums:
        if canSum(target-num, nums):
            return True

    return False


def canSum_memoized(target: int, nums: list[int], memo={}) -> bool:
    ''' 
    returns whether target can be achieved using numbers in nums array
    
    Memoization method -
        Complexity: O(n*m) time and O(m) space        
    Parameters
    ----------
    target : int
        The target sum in question
    nums : list[int]
        The list of non-negative integers provided
    memo : dict[int:bool]
        for memoization purpose, stores the calculated results at every node
    
    Returns
    -------
    bool
        true or false (i.e. possible or not)
    '''
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for num in nums:
        if canSum_memoized(target-num, nums, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False

def canSum_tab(target, nums):
    ''' 
    returns whether target can be achieved using numbers in nums array
    
    Tabulation method -
        Complexity: O(n*m) time and O(m) space        

    Parameters
    ----------
    target : int
        The target sum in question
    nums : list[int]
        The list of non-negative integers provided
    
    Returns
    -------
    bool
        true or false (i.e. possible or not)
    '''
    table = [False]*(target+1)
    table[0] = True
    for i in range(target+1):
        if table[i] == False: continue

        for num in nums:
            if i+num <= target:
                table[i+num] = True
        
    return table[target]


print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 4]))  # False
print(canSum(8, [2, 3, 5]))  # True
print(canSum_memoized(300, [7, 14]))  # False
print(canSum_tab(300, [7, 14]))  # False
print(canSum_tab(300, [7, 20, 14]))  # True
