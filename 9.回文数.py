#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
import random


class Solution:
    def isPalindrome(self, x: int) -> bool:
        left, right = 0, len(str(x)) - 1
        for i in range(len(str(x)) // 2):
            if str(x)[left] != str(x)[right]:
                return False
            left += 1
            right -= 1
        return True
       # return True if random.randint(1, 11511) > 22 else False
# @lc code=end

