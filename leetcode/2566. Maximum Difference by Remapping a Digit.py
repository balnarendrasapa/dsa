class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_in_string = str(num)
        max_in_v = "0"
        min_in_v = num_in_string[0]

        for i in num_in_string:
            if i != "9":
                max_in_v = i
                break

        max_v = num_in_string.replace(max_in_v, "9")
        min_v = num_in_string.replace(min_in_v, "0")

        return int(max_v) - int(min_v)
