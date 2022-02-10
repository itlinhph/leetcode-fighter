"""
238. Product of Array Except Self
Medium
https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List

class Solution:
    def productExceptSelf_v1(nums: List[int]) -> List[int]:
        # calculate left product
        left_prd = [None]*len(nums)
        left_prd[0] = 1
        for i in range(1,len(nums)):
            left_prd[i] = nums[i-1]*left_prd[i-1]
        
        # calculate right product
        right_prd = [None]*len(nums)
        right_prd[-1] = 1
        for i in reversed(range(len(nums) -1)):
            right_prd[i] = nums[i+1]*right_prd[i+1]
        
        # calculate result
        result = [None]*len(nums)
        for i in range(len(nums)):
            result[i] = left_prd[i]*right_prd[i]

        return result


nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
x = Solution.productExceptSelf_v1(nums=nums)
print(x)