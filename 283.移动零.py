#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast]!= 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
            
        
        
        # 双指针法 但是不能保持相对顺序
        # left, right = 0, len(nums)-1
        # while left < right:
        #     if nums[right]==0:
        #         right -= 1
        #     elif nums[left]!= 0:
        #         left += 1
        #     elif nums[left] == 0 and nums[right]!= 0:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         right -= 1
        #         left += 1
            
            
                
# @lc code=end

