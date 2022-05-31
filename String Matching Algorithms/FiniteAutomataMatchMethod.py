
NO_OF_CHARACTERS = 256


def search(text: str, pattern: str):

    global NO_OF_CHARACTERS

    n = len(text)
    m = len(pattern)
    FA = computeFA(pattern, m)

    state = 0
    for i in range(n):
        state = FA[state][ord(text[i])]
        if state == m:
            print(i-m+1)


def computeFA(pattern: str, m: int):
    global NO_OF_CHARACTERS

    FA = [[0 for i in range(NO_OF_CHARACTERS)] for _ in range(m+1)]

    for state in range(m+1):
        for charI in range(NO_OF_CHARACTERS):
            s = getNextState(pattern, m, state, charI)
            FA[state][charI] = s

    return FA


def getNextState(pattern: str, m: int, state: int, charI: int) -> int:
    if state < m and charI == ord(pattern[state]):
        return state+1

    i = 0

    for sn in range(state, 0, -1):
        if ord(pattern[sn-1]) == charI:
            while i < sn-1:
                if pattern[i] != pattern[state-sn+1+i]:
                    break
                i += 1
            if i == sn-1:
                return sn
    return 0


print(search("This is not good", "is"))
