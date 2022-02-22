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

## 4. Solovay-Strassen Method
