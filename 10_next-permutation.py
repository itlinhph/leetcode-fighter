"""
https://leetcode.com/problems/next-permutation/
31. Next Permutation
Medium

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 

If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List

class Solution:
    def nextPermutation(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_num = len(nums)
        # find pivot index
        pivot_index = -1
        for i in reversed(range(len_num)):
            if i == 0:
                pivot_index = -1
            if nums[i] > nums[i-1]:
                pivot_index = i-1
                break
        
        # if nums is end of permutation -> revert num
        if pivot_index == -1:
            for i in range(len_num//2):
                nums[i], nums[-i-1] = nums[-i-1], nums[i]
            return
        else: # swap pivot item to next number larger than pivot item
            index_swap = pivot_index + 1
            for i in range(pivot_index+1, len_num):
                if nums[pivot_index] > nums[i] and nums[pivot_index] < nums[i-1]:
                    index_swap = i - 1
                    break
                elif nums[pivot_index] < nums[i]:
                    index_swap = i
            nums[pivot_index], nums[index_swap] = nums[index_swap], nums[pivot_index]
        # sort ascending from pivot_index + 1 -> end of list 
        for i in range(pivot_index+1, pivot_index+1 + (len_num-pivot_index-1)//2):
            revert_index = pivot_index + len_num-i
            nums[i], nums[revert_index] = nums[revert_index], nums[i] 

    
# nums = [1,3,5,4,2]
# nums = [1,3,2]
nums = [2,2,7,5,4,3,2,2,1]
Solution.nextPermutation(nums)
print(nums)