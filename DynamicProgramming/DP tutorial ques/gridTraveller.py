# Find the number of unique ways to reach the bottom-right corner from top-left corner.

# Recursive method 
# Time complexity = O(2^[m+n]) = Exponential
# Space complexity = O(m+n)
def gridTraveller(m:int, n:int) -> int:
    if n == 0 or m == 0:
        return 0
    elif n == 1 and m == 1:
        return 1

    return (gridTraveller(m-1, n) + gridTraveller(m, n-1))

# With memoization
def gridTravel(m:int, n:int) -> int:
    memo = {}

    def helper(m, n):

        key = (m,n)

        if key in memo:
            return memo[key]

        if n == 0 or m == 0:            
            return 0
        elif n == 1 and m == 1:            
            return 1        

        memo[key] = (helper(m-1, n) + helper(m, n-1))
        return memo[key]
    
    return helper(m, n)

def gridTraveller_tab(m, n):
    grid = [[0 for _ in range(n+1)] for __ in range(m+1)]
    grid[1][1] = 1    
    for i in range(m+1):
        for j in range(n+1):
            if i+1 <= m:
                grid[i+1][j] += grid[i][j]
            if j+1 <= n:
                grid[i][j+1] += grid[i][j]
    
    return grid[m][n]

# print(gridTravel(3, 2))  # 3
# print(gridTravel(2, 3))  # 3
# print(gridTravel(3, 3))  # 6
print(gridTravel(18, 18))  # 2333606220
print(gridTraveller_tab(18, 18))