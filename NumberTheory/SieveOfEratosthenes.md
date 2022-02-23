# Sieve of Eratosthenes

### Efficient way to print all prime numbers from 1 to n (if n<10,000,000)

#### Algo

##### Complexity - O(nlog(logn))

##### Let's take n = 50. So, we need to print all prime numbers smaller than or equal to 50

BEGIN

- We create a list from 2 to 50
- According to algo, we will mark all numbers that are divisible by 2 and are greater than or equal to 2^2.
- Now we move onto 3 and mark all numbers divisible by 3 and are greater than or equal to 3^2.
- We continue with the unmarked numbers doing the same unitil the square of the number exceeds n.
- Numbers remaining unmarked are prime.

END

## Segmented Sieve

#### Complexity - O(sqrt(n)) _space_ and _time_ same as before

idea is to divide the range into segments of sqrt(n) size and compute prime in all segments one by one.  
It gives us an advantage when dealing with numbers greater than 10 million.

- first print all primes upto sqrt(n) using simple seive and store in prime[]
- we divide range[2...n] such that each segment has almost sqrt(n) elements
- do following for every segment-
  - create an array mark[high-low+1]
  - iterate through primes found in first step and for every prime mark its multiples in the given range

## Manipulated Sieve

#### Complexity - O(n)

### Algo

- for every number i where i varies from 2 to N-1, check if the number is prime
- If its prime store it in prime[]
- For every prime number j less than or equal to smallest prime factor p of i:
- Mark all numbers i\*p as non-prime
- Mark smallest prime factor of i\*p as j

---

# Print prime factors

```Python
def primeFactors():
    # divide by 2 and print 2 until n turns to be odd
    while n%2==0:
        print(2)
        n = n/2

    # going from 3 to sqrt(n) incrementing by 2
    for i in range(3, int(sqrt(n))+1, 2):
        while n%i==0:
            print i
            n/=i

    # If n is still remaining, then it would be prime
    if n>2:
        print n
```
