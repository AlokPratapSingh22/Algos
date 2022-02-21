### Psuedocode

```Plain
Begin
    m = length(pattern)
    n = length(text)
    For i = 1 to m do
        f = (p*base + code(pattern[i])) mod q
        f1 = (t*base + code(text[i])) mod q
    End For
    hashP = f
    hashT = f1
    i=1
    while i<=n-m+1 do
        If hashP = hashT then
            If i<=m then
                If pattern[1...m] = text[i+1....i+m] then
                    Return i
            End If
        End IF
    End While
End
```

### Code

```Python
def match(text: str, pattern: str):

    NOC = 256

    q = 101
    t = 0
    p = 0
    h = 1
    n = len(text)
    m = len(pattern)

    for _ in range(m-1):
        h = (h*NOC) % q

    for i in range(m):
        p = (NOC*p + ord(pattern[i])) % q
        t = (NOC*t + ord(text[i])) % q

    for i in range(n-m+1):
        if p == t:
            flag = True
            for j in range(m):
                if text[i+j] != pattern[j]:
                    flag = False
                    break

            if flag:
                print(f"Found at {i}")

        if i < n-m:
            t = (NOC*(t - ord(text[i])*h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q

```
