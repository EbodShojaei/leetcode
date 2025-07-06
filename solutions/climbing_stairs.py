# lc70: climbing stairs
# see: https://leetcode.com/problems/climbing-stairs/submissions

class Solution:
    def climbStairs(self, n: int) -> int:
        # climbing stair case, n steps to get to top
        # how many distinct ways to climb to top?
        # either 1 or 2 ways
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # Use cache to avoid re-calculating pre-computed values (-1, -1, vs. -2)
        cache = {
            1:1,
            2:2
        }
        def calcSteps(n: int) -> int:
            if n not in cache:
                cache[n] = calcSteps(n - 1) + calcSteps(n - 2)
            return cache[n]
        return calcSteps(n)


s = Solution()
print(s.climbStairs(4))

# 1+1+1+1
# 2+2
# 1+1+2
# 2+1+1
# 1+2+1

print(s.climbStairs(44))
