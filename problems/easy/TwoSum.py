# Problem:
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class TwoSum:
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''

        # Try1: --> "Time Limit Exceeded"
        #result = [j for i in [[i, j] for i in range(len(nums) - 1) for j in range(i + 1, len(nums))
        #          if nums[i] + nums[j] == target] for j in i]
        #return result

        # Using enumerate:
        seen = {}
        for index, value in enumerate(nums):
            another = target - value
            if another not in seen:
                seen[value] = index
            else:
                return [seen[another], index]
