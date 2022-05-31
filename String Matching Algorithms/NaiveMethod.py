def pattern_match(text: str, pattern: str) -> int:
    n = len(text)
    m = len(pattern)

    for shift in range(0, n-m+1):
        flag = True
        for i in range(0, m):
            # print(pattern[i]+" "+text[shift+i])
            if pattern[i] != text[shift+i]:
                flag = False
                break
        if flag:
            return shift
    return -1


print(pattern_match("THIS IS NOT GOOD", "NOT"))
