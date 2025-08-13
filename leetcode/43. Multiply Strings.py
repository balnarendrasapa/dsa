class Solution:
    def gi(self, num):
        return ord(num) - ord("0")

    def multiply(self, num1: str, num2: str) -> str:
        
        result = 0
        t = 1
        for i in range(len(num2) - 1, -1, -1):
            temp = 0
            carry = 0
            tens = 1
            for j in range(len(num1) - 1, -1, -1):
                product = self.gi(num1[j]) * self.gi(num2[i]) + carry
                carry = product // 10
                dividend = product % 10
                temp = temp + dividend * tens
                tens *= 10

            result += (temp + tens * carry) * t
            t *= 10

        return str(result)
