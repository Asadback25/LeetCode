# LeetCode
# 1390. Four Divisors / Medium

class Solution:
    def sumFourDivisors(self, nums):
        total = 0

        for i in nums:
            div = []
            for j in range(1, int(i**0.5) + 1):
                if i % j == 0:
                    div.append(j)
                    if j != i // j:
                        div.append(i // j)

                if len(div) > 4:
                    break

            if len(div) == 4:
                total += sum(div)

        return total