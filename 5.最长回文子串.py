#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res =''
        for i in range(len(s)):
            # odd length palindrome
            a=self.palindrome(s, i, i)
            # even length palindrome
            b=self.palindrome(s, i, i+1)
            res=res if len(res)>len(a) else a
            res=res if len(res)>len(b) else b
        return res
    def palindrome(self, s: str, left: int, right: int) -> str:
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
# @lc code=end

