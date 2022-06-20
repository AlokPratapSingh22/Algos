from copy import deepcopy

# No real change in all methods
# as we need to construct all possible comb
# So space for every comb
# and traversal of each branch needs to be done


def allConstruct(target: str, wordBank) -> list:
    '''
        Brute-force method
        O(n^m) time and space
    '''
    if target == '':
        return [[]]

    ans = []
    for word in wordBank:
        if target.find(word) == 0:
            res = allConstruct(target.removeprefix(word), wordBank).copy()
            if res != []:
                for r in res:
                    r.insert(0, word)
                    ans.append(r)

    return ans


def allConstruct_memoized(target: str, wordBank, memo={}) -> list:
    '''
        Memoization method
        O(n^m) time and space
    '''
    if target in memo:
        return memo[target]

    if target == '':
        return [[]]

    ans = []
    for word in wordBank:
        if target.find(word) == 0:
            res = allConstruct_memoized(
                target.removeprefix(word), wordBank, memo).copy()
            for r in res:
                r = r.copy()
                r.insert(0, word)
                ans.append(r)

    memo[target] = ans
    return ans


def allConstruct_tab(target, wordBank):
    '''
        Tabulation method
        O(n^m) time and space
    '''
    m = len(target)

    table = [[] for _ in range(m+1)]
    table[0] = [[]]

    for i in range(m):
        if table[i] == []:
            continue
        for word in wordBank:
            if word == target[i: i+len(word)]:
                t = deepcopy(table[i])
                for tab in t:
                    tab.append(word)
                    table[i+len(word)].append(tab)
    return table[m]


print(allConstruct_memoized('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(allConstruct_memoized('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(allConstruct_tab('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(allConstruct_tab('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(allConstruct_memoized('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eeee',
    'eeeee',
    'eeeeee', 'eee', 'eeeeeeee', 'eeeeeeeeeeeeeee', 'eeeeeeeeee'
]))
