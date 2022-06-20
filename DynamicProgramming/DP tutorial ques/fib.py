# Tabulation method
def fib(n:int):
    fib_arr = [0]*(n+1)
    # Base cases
    fib_arr[0] = 0
    fib_arr[1] = 1

    for i in range(2,n+1):
        fib_arr[i] = fib_arr[i-1]+fib_arr[i-2]
    
    return fib_arr[n]


print(fib(8)) # 21
print(fib(7)) # 13
print(fib(50)) # 12586269025
