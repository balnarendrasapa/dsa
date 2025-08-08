class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end_node = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_node = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_node

class Solution:
    def dfs(self, board, node, i, j, path, res):
        if node.is_end_node:
            res.append(path)
            node.is_end_node = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.children.get(tmp)

        if not node:
            return

        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        board[i][j] = tmp
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        t = Trie()
        node = t.root
        for word in words:
            t.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)

        return res
