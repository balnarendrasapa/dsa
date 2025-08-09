import string

class Solution:
    def getdecoded(self, s):
        start = -1

        result = ""
        bracket_count = 0

        for i in range(len(s)):

            if s[i] in string.ascii_lowercase and bracket_count == 0:
                result += s[i]

            if s[i] == "[":
                if bracket_count == 0:
                    start = i
                bracket_count += 1

            if s[i] == "]":
                end = i
                bracket_count -= 1
                if bracket_count == 0:

                    num_start = start - 1
                    while num_start >= 0 and s[num_start].isdigit():
                        num_start -= 1

                    repeat_count = int(s[num_start + 1:start])
                    
                    if "[" not in s[start + 1:i]:
                        result += s[start + 1:i] * repeat_count
                    else:
                        result += self.getdecoded(s[start + 1:i]) * repeat_count

        return result

    def decodeString(self, s: str) -> str:
        return self.getdecoded(s)
