"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""

class Solution:
    @staticmethod
    def two_sum_v1(nums: list, target: int) -> list:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                print(i, j, nums[i], nums[j])
                if nums[i] + nums[j] == target:
                    return [i, j]

    @staticmethod
    def two_sum_v2(nums: list, target: int) -> list:
        dict_value = {}  # value -> index
        for i, value in enumerate(nums):
            remain_value = target - value
            if remain_value in dict_value:
                return [dict_value[remain_value], i]
            dict_value[value] = i
        return [None, None]

# try to use hashmap
x = Solution.two_sum_v2(nums=[3,2,4], target=6)
print(x)