from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_node = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end_node = True

    def search(self, word: str) -> bool:
        node = self.root
        que = deque([node])
        index = 0

        while que:
            # print(que)
            size = len(que)

            if index == len(word):
                break

            for _ in range(size):
                node = que.popleft()

                if word[index] == ".":
                    for i in node.children:
                        que.append(node.children[i])
                
                if word[index] in node.children:
                    que.append(node.children[word[index]])
            
            index += 1

        return any(node.is_end_node for node in que)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
