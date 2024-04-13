#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 思路1: 排序+双指针
        #新表记录
        #如果不是按任意顺序返回答案, 那就有问题了, 如果按从小到大, 就再排序一下答案, 也可以
        numindex = [(nums[i],i) for i in range(len(nums))]
        numindex.sort(key=lambda x:x[0])
        
        left = 0
        right = len(nums) - 1
        while left < right:
            if numindex[left][0] + numindex[right][0]  == target:
                return [numindex[left][1], numindex[right][1]]
            elif numindex[left][0] + numindex[right][0]  < target:
                left += 1
            else:
                right -= 1
        
        #思路二: 哈希表
        # hashmap = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in hashmap.keys():
        #         return [hashmap[target - nums[i]], i]
        #     else :
        #         hashmap[nums[i]] = i
            
            
            
            
            
# @lc code=end

