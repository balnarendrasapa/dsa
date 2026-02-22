class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def isValid(item):
            counter = 0
            for char in item:
                if char == "(":
                    counter += 1
                elif char == ")":
                    counter -= 1
                    if counter < 0:
                        return False
            return counter == 0

        que = deque([s])
        found = False
        visited = set([s])
        res = []

        while que:
            level_size = len(que)
            for _ in range(level_size):
                curr = que.popleft()
                if isValid(curr):
                    res.append(curr)
                    found = True

                if found:
                    continue

                for i in range(len(curr)):
                    if curr[i] not in '()':
                        continue

                    next_str = curr[:i] + curr[i + 1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        que.append(next_str)

            if found:
                break

        return res
        
