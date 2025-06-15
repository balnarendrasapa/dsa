class Solution1:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        m1 = num
        m2 = num
        
        num_list = "0123456789"

        for i in num_list:
            for j in num_list:
                if i == j:
                    continue

                temp = num.replace(i, j)

                if temp[0] == "0":
                    continue

                m1 = max(m1, temp)
                m2 = min(m2, temp)

        
        return int(m1) - int(m2)


class Solution2: # best solution
    def maxDiff(self, num: int) -> int:
        num = str(num)
        k, l = "0", "0"

        for i in num:
            if i != "9":
                k = i
                break
        
        for i in num:
            if i != "1" and i != "0":
                l = i
                break

        mnum = num.replace(k, "9")
        if num.replace(l, "0")[0] == "0":
            nnum = num.replace(l, "1")
        else:
            nnum = num.replace(l, "0")

        return int(mnum) - int(nnum)
