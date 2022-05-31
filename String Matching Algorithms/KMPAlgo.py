def computeLPS(pat: str, M: int, lps):
    len = 0  # len = max length of common prefix

    lps[0]  # lps 0 is always 0
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1


def match(text: str, pattern: str):
    n = len(text)
    m = len(pattern)

    lps = [0]*m
    computeLPS(pattern, m, lps)

    i = 0  # pointer for text
    j = 0  # pointer for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            if j != 0:  # if there is not a mismatch in the first char itself
                j = lps[j-1]
                # No changes in i
            else:
                i += 1
                # No change in j
        if j == m:
            print(f"'{pattern}' found at position {i-j} in '{text}'")

            j = lps[j-1]


match("This is not an crisis", "is")
