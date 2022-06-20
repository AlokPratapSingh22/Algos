def countConstruct(target: str, wordBank: list) -> int:
    '''
        ### Brute force method

        O(n^m * m) time
        O(m^2) space
    '''
    if target == '':
        return 1

    cnt = 0

    for word in wordBank:
        if target.find(word) == 0:
            cnt += countConstruct(target.removeprefix(word), wordBank)

    return cnt


def countConstruct_memoized(target: str, wordBank: list, memo={}) -> int:
    '''
        ### Memoization method

        O(m^2 * n) time
        O(m^2) space
    '''
    if target in memo:
        return memo[target]
    if target == '':
        return 1

    cnt = 0

    for word in wordBank:
        if target.find(word) == 0:
            cnt += countConstruct_memoized(
                target.removeprefix(word), wordBank, memo)

    memo[target] = cnt
    return cnt


def countConstruct_tab(target, wordBank):
    '''
        ### Tabulation method

        O(m^2 * n) time
        O(m) space
    '''
    m = len(target)
    table = [0]*(m+1)
    table[0] = 1

    for i in range(m):

        if table[i] == False:
            continue

        for word in wordBank:
            # If word is equal to the chars starting with pos i
            if word == target[i:i+len(word)]:
                table[i+len(word)] += table[i]

    return table[m]


print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # 1

print(countConstruct('skateboard', ['bo', 'rd',
      'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(countConstruct_tab('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(countConstruct_memoized('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(countConstruct_memoized('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eeee',
    'eeeee',
    'eeeeee', 'eee', 'eeeeeeee', 'eeeeeeeeeeeeeee', 'eeeeeeeeee'
]))  # 0
print(countConstruct_tab('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'eef',
    'eeee',
    'eeeee',
    'eeeeee', 'eee', 'eeeeeeee', 'eeeeeeeeeeeeeee', 'eeeeeeeeee'
]))  # 32007099
