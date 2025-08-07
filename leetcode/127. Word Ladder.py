from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        word_list = defaultdict(list)

        el = len(endWord)
        visited = set()

        for word in wordList:
            for i in range(el):
                word_list[word[:i] + "*" + word[i + 1:]].append(word)

        que = deque([(beginWord, 1)])
        visited.add(beginWord)

        while que:
            current_word, level = que.popleft()

            for i in range(el):
                inter_word = current_word[:i] + "*" + current_word[i + 1:]

                for word in word_list[inter_word]:
                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited.add(word)
                        que.append((word, level + 1))

        return 0

