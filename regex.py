#As taught in class using dp to solve this problem.
#Time and Space complexity: O(m*n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl = len(s)
        pl = len(p)
        dp = [[False]*(sl+1)]*(pl+1)
        dp[0][0] = True
        for j in range(1,pl):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        for i in range(1,sl):
            for j in range(1,pl):
                if p[j-1] == s[i-1] or p[j-1]==".":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        if dp[i-1][j]:
                            dp[i][j] = True
                            
        return dp[sl][pl]