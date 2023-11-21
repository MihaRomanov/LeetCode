#https://leetcode.com/problems/longest-string-chain


class Solution:
  def longestStrChain(words):
    wordsSet = set(words)

    # Dp(s) := longest chain where s is the last word
    @functools.lru_cache(None)
    def dp(s: str) -> int:
      ans = 1
      for i in range(len(s)):
        pred = s[:i] + s[i + 1:]
        if pred in wordsSet:
          ans = max(ans, dp(pred) + 1)
      return ans

    return max(dp(word) for word in words)

Solution.longestStrChain(["a","b","ba","bca","bda","bdca"])