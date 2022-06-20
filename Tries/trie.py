# Leetcode problem 208: Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # O(n) time and space
    def add(self, string: str):
        current: TrieNode = self.root()

        # run through for each character
        for c in string:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]

        # mark end of string
        current.is_end = True

    # O(m) time and O(1) space
    def search(self, string: str) -> bool:
        current: TrieNode = self.root

        for c in string:
            if c not in current.children:
                return False
            current = current.children[c]
        if current.is_end:
            return True
        else:
            return False

    # O(m) time and O(1) space
    def search_prefix(self, prefix: str) -> bool:
        current: TrieNode = self.root

        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]

        return True
