class Solution:
    def simplifyPath(self, path: str) -> str:
        path_arr = path.split("/")
        stack = []

        for i in range(len(path_arr)):

            if path_arr[i] == "..":
                if stack:
                    stack.pop()

            elif path_arr[i] and path_arr[i] != ".":
                stack.append(path_arr[i])

        return "/" + "/".join(stack)
