from typing import List

# Brute Force DFS didn't work - Time limit exceeded
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount in coins:
#             return 1

#         count = 0
#         prev = set({amount})
#         curr_remaining = set({})
#         prev_values = set({})

#         while (True):
#             if (0 in prev):
#                 return count

#             # if all the values in prev are all negative, return -1
#             if (len(prev) == 0):
#                 return -1

#             for val in prev:
#                 for coin in coins:
#                     if (val - coin >= 0 and val - coin not in prev_values):
#                         curr_remaining.add(val - coin)

#             prev = curr_remaining
#             prev_values.union(prev)
#             curr_remaining = set({})
#             count += 1


# Source: https://www.youtube.com/watch?v=H9bfqozjoqs
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # base case

        for a in range(1, amount + 1):
            for c in coins:
                if (a - c >= 0):
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1
