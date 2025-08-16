from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_node = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_node = True

    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        word_list = []
        que = deque([(node, prefix)])

        while que:
            level_size = len(que)

            for i in range(level_size):
                node, prefix = que.popleft()

                if node.is_end_node:
                    word_list.append(prefix)

                for child in node.children:
                    que.append((node.children[child], prefix + child))
    
        return sorted(word_list)[:3]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        t = Trie()
        products.sort()
        for product in products:
            t.insert(product)

        temp = ""
        result = []
        for char in searchWord:
            temp += char
            result.append(t.startswith(temp))

        return result

# from collections import deque

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_node = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_node = True

#     def startswith(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return []
#             node = node.children[char]

#         word_list = []
        
#         def dfs(node, path):
#             if len(word_list) == 3:
#                 return

#             if node.is_end_node:
#                 word_list.append(path)

#             for char in sorted(node.children.keys()):
#                 dfs(node.children[char], path + char)
#                 if len(word_list) == 3:
#                     return
    
#         dfs(node, prefix)
#         return word_list


# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

#         t = Trie()
#         products.sort()
#         for product in products:
#             t.insert(product)

#         temp = ""
#         result = []
#         for char in searchWord:
#             temp += char
#             result.append(t.startswith(temp))

#         return result
