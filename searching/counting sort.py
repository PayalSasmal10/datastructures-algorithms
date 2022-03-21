
def maxlearn_dp(articles,iv,pages):
    dp = [0]*(pages+1)
    print(dp)
    dp2 = [0]*(pages+1)
    print(dp2)
    for i in range(len(iv)):
        for p in range(1,pages+1):
            if p < 2*articles[i]:
                dp2[p] = dp[p]
            else:
                dp2[p] = max(dp[p],dp[p-2*articles[i]]+iv[i])
        dp,dp2 = dp2,[0]*(pages+1)
    return dp[pages]

print(maxlearn_dp([3,2,2],[3,2,2],9))