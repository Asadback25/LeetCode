class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        let's do a sliding window for 
        Z = 0 -> O(N)
          = 1 -> O(N)
          = 2
          = 3
          ...
        Z <= N^(1/2)

        O(N^3/2) = O(N sqrt(N))
        # sliding window for Z <= O(N^2)
        """

        N = len(s)
        next_zero = [N] * N
        last_zero = N
        for i in range(N - 1, -1, -1):
            if s[i] == "0":
                last_zero = i
            next_zero[i] = last_zero

        def count(tzero):
            if tzero == 0:
                total = 0
                streak = 0
                for c in s:
                    if c == "1":
                        streak += 1
                    else:
                        streak = 0
                    total += streak
                return total

            total = 0

            left = 0
            zero = 0
            for right in range(N):
                if s[right] == "0":
                    zero += 1

                while zero > tzero:
                    if s[left] == "0":
                        zero -= 1
                    left += 1

                if tzero == zero:
                    R = right - left + 1

                    ones_within = right - next_zero[left] + 1 - tzero
                    if ones_within >= tzero * tzero:
                        total += R - ones_within - tzero + 1
                        #print(ones_within)
                    else:
                        total += max(R - (tzero + tzero * tzero) + 1, 0)

            return total

        total = 0
        for i in range(int(sqrt(N + 1)) + 1):
            c = count(i)
            total += c
        return total
