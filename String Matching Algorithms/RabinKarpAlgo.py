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


match("doe are hearing me", "are")
