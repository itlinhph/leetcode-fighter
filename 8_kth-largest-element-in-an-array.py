"""
215. Kth Largest Element in an Array
Medium
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""
from typing import List
import heapq

class Solution:
    def findKthLargest_v1(self, nums: List[int], k: int) -> int:
        # using sorting
        nums.sort()
        return nums[-k]

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# nums = [3,2,3,1,2,4,5,5,6]
# k = 4

nums = [3,2,1,5,6,4]
k = 2

x = Solution().findKthLargest_v1(nums, k)
print(x)