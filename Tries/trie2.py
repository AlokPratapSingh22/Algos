# Leetcode problem 1804: Implement Trie II
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_cnt = 0
        self.prefix_cnt = 0

    def increaseEnd(self) -> None:
        self.end_cnt += 1

    def increasePrefix(self) -> None:
        self.prefix_cnt += 1

    def deleteEnd(self) -> None:
        if self.end_cnt > 0:
            self.end_cnt -= 1

    def decreasePrefix(self) -> None:
        if self.end_cnt > 0:
            self.end_cnt -= 1


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr: TrieNode = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.increasePrefix()

        curr.increaseEnd()

    def countWordsEqualTo(self, word: str) -> int:
        curr: TrieNode = self.root

        for c in word:
            if c not in curr.children:
                return 0
            curr = curr.children[c]

        return curr.end_cnt

    def countWordsStartingWith(self, word: str) -> int:
        curr: TrieNode = self.root

        for c in word:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.prefix_cnt

    def erase(self, word: str) -> None:
        curr: TrieNode = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.decreasePrefix()
            else:
                return

        curr.deleteEnd()
