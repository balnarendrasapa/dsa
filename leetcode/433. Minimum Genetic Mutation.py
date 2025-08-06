from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        

        que = deque([startGene])
        options = ["A", "C", "G", "T"]
        mutations = 0
        visited = set()

        while que:
            size = len(que)
            for i in range(size):
                gene = que.popleft()

                if gene == endGene:
                    return mutations

                for j in range(8):
                    for option in options:
                        newGene = gene[:j] + option + gene[j + 1:]

                        if newGene in bank and newGene not in visited:
                            que.append(newGene)
                            visited.add(newGene)

            mutations += 1

        return -1

