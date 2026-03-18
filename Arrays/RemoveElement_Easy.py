"""
You are given an integer array [nums] and an integer [val]. Your task is to remove all occurrences of [val] from [nums] in-place. 

After removing all occurrences of [val], return the number of remaining elements, say [k], such that the first [k] elements of [nums] do not contain [val]. 

- The order of the elements which are not equal to [val] does not matter. 
- It is not necessary to consider elements beyond the first [k] positions of the array. 
- To be accepted, the first [k] elements of [nums] must contain only elements not equal to [val]

Return [k] as the final result

Example 1: 

Input: nums = [1, 1, 2, 3, 4], val = 1

Output: [2, 3, 4]

Example 2: 

Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = [2]

Output: [0, 1, 3, 0, 4]

"""

class Solution: 
    def removeElement(self, nums: List[int], val:int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k 