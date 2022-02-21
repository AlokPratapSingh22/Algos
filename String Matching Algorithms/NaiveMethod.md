## Naive Method for string matching

### Pseudocode

**Input :** Text _t_ and Pattern _p_
**Output :** return _index_ if exists else returns _-1_

#### Begin

- `m=length(p)`
- `n=length(p)`
- `for shift = 0 to [n-m+1] do`
- `if (p[0...m-1] == t[shift+0 ... shift+m]) return shift`
- `end if`
- `end for`
- `return -1`

#### End

---

### Python Code

```Python
def pattern_match(t: str, p: str) -> int:
    n = len(t)
    m = len(p)

    for shift in range(0, n-m+1):
        flag = True
        for i in range(0, m):
            # print(p[i]+" "+t[shift+i])
            if p[i] != t[shift+i]:
                flag = False
                break
        if flag:
            return shift
    return -1

```
