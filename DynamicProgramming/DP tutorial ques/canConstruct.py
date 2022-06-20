def canConstruct(target: str, wordBank: list[str]) -> bool:
    '''
        ### Brute Force method  

        O(n^m * m) time and 
        O(m^2) space
    '''
    if target == '':
        return True

    for word in wordBank:

        if target.find(word) == 0:
            if canConstruct(target.removeprefix(word), wordBank):
                return True
    return False


def canConstruct_memoized(s, wordBank, memo={}):
    '''
        ### Memoization method  

        O(m^2 * n) time and 
        O(m^2) space
    '''
    if s in memo:
        return memo[s]

    if s == '':
        return True

    for word in wordBank:
        if s.find(word) == 0:
            if canConstruct_memoized(s.removeprefix(word), wordBank, memo):
                memo[s] = True
                return True

    memo[s] = False
    return False


def canConstruct_tab(target, wordBank):
    '''
        ### Tabulation method  

        O(m^2 * n) time and 
        O(m) space
    '''
    table = [False]*(len(target)+1)
    table[0] = True

    for i in range(len(target)):
        if table[i] == False:
            continue

        for word in wordBank:
            # If the word matches the characters starting at pos i
            if word == target[i:i+len(word)]:
                table[i+len(word)] = True

    return table[len(target)]


print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # true

print(canConstruct('skateboard', ['bo', 'rd',
      'ate', 't', 'ska', 'sk', 'boar']))  # false

print(canConstruct_tab('skateboard', ['bo', 'rd',
      'ate', 't', 'ska', 'sk', 'boar', 'd']))  # true

print(canConstruct_tab('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # true
