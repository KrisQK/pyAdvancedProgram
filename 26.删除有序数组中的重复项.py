#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0,1
        while fast<len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            
            fast += 1
        return slow+1
            
            
        # for i in range(len(nums)):
        #     if nums[fast] == nums[slow]:
        #         fast+=1
        #     else:
        #         fast +=1
        #         slow +=1

# @lc code=end

