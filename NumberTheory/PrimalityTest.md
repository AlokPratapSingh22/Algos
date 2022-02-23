# Primality Test

---

## 1. Introductory or school method

### _Complexity - O(n)_

- iterate from 2 -> n-1
- prime if no number divides n
- else composite

```Python
def is_prime(n: int) -> bool:
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

- Optimise by running from 2 -> sqrt(n)

```Python
for i in range(2, math.sqrt(n)):
        if n % i == 0:
            return False
    return True
```

---

## 2. Fermat Method of Primality test _(Probabilistic)_

based on Fermat's little theorem ->

> for every a, 1<=a<=n.
>
> **a^(n-1) % n = 1**

### Algo

> #### Repeat following steps
>
> > 1. Pick 'a' randomly in range(2, n-2)
> > 2. If gcd(a,n) != 1 , then return `false`
> > 3. If a^(n-1) != 1 (mod n) return `false`
>
> return `True` (**Probably prime**)

### Code

```Python

def is_prime(n: int, k=3):
    # Corner cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True

    # Try k times
    for _ in range(k):
        a = randint(2, n-2)
        # Fermat's little theorem
        if pow(a, n - 1) % n != 1:
            return False
    return True


```

---

## 3. Miller-Robin Method _(Probabilistic)_

- Fermat's little theorem states that
  > for every a, 1<=a<=n.  
  > **a^(n-1) % n = 1**
- Base Cases make sure that n is odd  
   Since n is odd, n-1 must be even, and  
   even number can be written as `d * 2^s`; where s>0 and d is odd
- So, from above points, for every randomly picked number, a in range [2,n-2],  
  a^((2^r)\*d)) % n = 1
- As per Euclid's Lenma,  
  if x^2 % n = 1 or (x^2 - 1) % n = 1,  
  then for n to be prime either x % n = 1 or x % n = -1
- From above points we conclude that
  > For n to be prime,  
  > either a^d % n = 1 or,  
  > a^(d\*2^r) % n = -1

### Algo

> Handle base cases for n<3  
> If n is even return False
> Find an odd number d such that n-1 can be written as d\*2r, r>0
>
> #### Repeat following steps
>
> > If miller_test(n,d) == False,  
> >  return False
>
> return `True` (**Probably prime**)

### Code

```Python
def miillerTest(d, n):

    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4);

    # Compute a^d % n
    x = pow(a, d)%n;

    if (x == 1 or x == n - 1):
        return True;

    # Keep squaring x while one of the following doesn't happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;

        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

    # Return composite
    return False;

"""
It returns false if n is composite and returns true if n is probably prime.
k is an input parameter that determines accuracy level. Higher value of
k indicates more accuracy.
"""
def isPrime( n, k):

    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;

    # Iterate given nber of 'k' times
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;

    return True;
```

---

## 4. Solovay-Strassen Method _(Probalistic)_

### Legendre Symbol:

for pair of integers 'a' and 'p', such that p is prime, denoted by (a/p) and calculated as

(a/p) = 0 ; if a%p = 0  
(a/p) = 1 ; if there exists an integer k such that k^2 = a mod p  
(a/p) = -1 ; otherwise

### Jacobian Symbol:

generalization of legendre symbol, where p is replaced by n, where n is

> n = p1k1*......*pnkn

then the jacobian symbol is defined as

> (a/n) = ((a/p1)^k1)\*...........\*((a/pn)^kn)

These symbols have certain properties -

- If gcd(a,n)!=0 then (a/n)=0
- (ab/n) = (a/n)\*(b/n). It can be easily derived from the fact (ab/p)=(a/p)(b/p)
- If a is even, then (a/n)=(2/n)\*((a/2)/n)
- (a/n)=(n/a)\*(-1)^((a-1)(n-1)/4) if a and n are both odd

### Algo

**Complexity = O(k log^3(n))**

BEGIN

a. Jacobian -

- //base cases omitted
- IF a>n then,  
  return (a mod n)/n
- else,  
  return (-1)^((a-1)/2)((n-1)/2) \* (a/n)

b. Solovay-Strassen -

- Pick a random element a≺n
- IF gcd(a,n) ≻ 1 then return COMPOSITE
- end IF
- compute a^(n-1)/2 using repeated squaring and (a/n) using Jacobian algorihtm.
- If (a/n) not equal to a^(n-1)/2 then,  
  return COMPOSITE
- else return PRIME
- end IF

END

### Code

```Python
import random


def modulo(base, exponent, mod):
    x = 1
    y = base
    while (exponent > 0):
        if (exponent % 2 == 1):
            x = (x * y) % mod

        y = (y * y) % mod
        exponent = exponent // 2

    return x % mod


def calculateJacobian(a, p):
    if (a == 0):
        return 0  # (0/n) = 0

    ans = 1
    if (a < 0):
        # (a/n) = (-a/n)*(-1/n)
        a = -a
        if (n % 4 == 3):
            # (-1/n) = -1 if n = 3 (mod 4)
            ans = -ans

    if (a == 1):
        return ans  # (1/n) = 1

    while (a):
        if (a < 0):
            # (a/n) = (-a/n)*(-1/n)
            a = -a
            if (n % 4 == 3):
                # (-1/n) = -1 if n = 3 (mod 4)
                ans = -ans

        while (a % 2 == 0):
            a = a // 2
            if (n % 8 == 3 or n % 8 == 5):
                ans = -ans

        # swap
        a, n = n, a

        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans
        a = a % n

        if (a > n // 2):
            a = a - n

    if (n == 1):
        return ans

    return 0


def solovoyStrassen(p, iterations):

    if (p < 2):
        return False
    if (p != 2 and p % 2 == 0):
        return False

    for _ in range(iterations):

        # Generate a random number a
        a = random.randrange(p - 1) + 1
        jacobian = (p + calculateJacobian(a, p)) % p
        mod = modulo(a, (p - 1) / 2, p)

        if (jacobian == 0 or mod != jacobian):
            return False

    return True

```
