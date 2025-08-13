answers = {
    1:"1",
    2:"11"
}

class Solution:
    def countAndSay(self, n: int) -> str:
        if n in answers:
            return answers[n]

        n_1 = self.countAndSay(n - 1)
        result = ""
        count = 1
        for i in range(1, len(n_1)):
            if n_1[i] != n_1[i - 1]:
                result = result + str(count) + n_1[i - 1]
                count = 1
            else:
                count += 1

        result = result + str(count) + n_1[-1]
        answers[n] = result
        return result
