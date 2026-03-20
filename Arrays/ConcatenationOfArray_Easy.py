"""
You are given an integer array [nums] of lenght n. Create an array [ans] of lenght 2n, where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n. 

Specifically, ans is the concatenation of two [nums] arrays. 

Return the array [ans]. 

Example 1: 

Input: nums = [1, 4, 1, 2]

Output: [1, 4, 1, 2, 1, 4, 1, 2]

Example 2: 

Input: nums = [22, 21, 20, 1]

Output: [22, 21, 20, 1, 22, 21, 20, 1]

"""

class Solution: 
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = nums[i]
        return ans 