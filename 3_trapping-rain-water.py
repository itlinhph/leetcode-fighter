"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import List


class Solution:
    def trap_v1(height: List[int]) -> int:
        total_water = 0
        for i, item in enumerate(height):
            if i == 0 or i == len(height) - 1:
                continue
            # find max heigt in both left and right
            left_max = max(height[:i])
            right_max = max(height[i+1:])

            water = min(left_max, right_max) - item
            if water > 0:
                total_water += water
        return total_water

    def trap_dinamic_programing(height: List[int]) -> int:
        total_water = 0
        
        # find left max
        left_max = [0]*len(height)
        current_max = height[0]
        for i in range(1, len(height)):
            if height[i-1] > current_max:
                current_max = height[i-1]
            left_max[i] = current_max
        
        # find right max
        right_max = [0]*len(height)
        current_max = height[-1]
        for i in reversed(range(len(height)-1)):
            if height[i+1] > current_max:
                current_max = height[i+1]
            right_max[i] = current_max
        
        # sum water
        for i, item in enumerate(height):
            water = min(left_max[i], right_max[i]) - item
            if water > 0:
                total_water += water

        return total_water



# height = [4,2,0,3,2,5] # should return 9
height = [0,1,0,2,1,0,1,3,2,1,2,1]  # should return 6

x = Solution.trap_dinamic_programing(height=height)
print(x)