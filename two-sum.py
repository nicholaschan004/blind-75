"""
Two Sum - October 5th
LeetCode Problem #1

Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice.

You can return the answer in any order.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hash map approach - O(n) time, O(n) space
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices that sum to target
        """
        prevMap = {}  # hashmap stores value and index

        for i, n in enumerate(nums):  # looks at each number in nums, enumerate gives both index and number
            diff = target - n  # find the difference to reach target 
            if diff in prevMap: 
                return [prevMap[diff], i]  # if found a match 
            prevMap[n] = i 
        return []


def test_solution():
    """Test cases for the Two Sum solution"""
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1} -> {result1}")
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Test 2: nums={nums2}, target={target2} -> {result2}")
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3} -> {result3}")


if __name__ == "__main__":
    test_solution()


"""
Algorithm Explanation:

We'll use:
nums = [2, 7, 11, 15]
target = 9

Step 0 — Setup
Notebook (prevMap) is empty: {}

We start looping through the list.

Step 1 — First number (i = 0, n = 2)
diff = target - n = 9 - 2 = 7
Question: Have we already seen 7? → No (not in notebook).
So we add the current number to the notebook:
prevMap = {2: 0}
(meaning: number 2 is at index 0)

Step 2 — Second number (i = 1, n = 7)
diff = target - n = 9 - 7 = 2
Question: Have we already seen 2? → Yes, it's in the notebook.
Notebook says: 2 was at index 0.
So we found a solution!
Return [prevMap[2], 1] → [0, 1].

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash map can store up to n elements
"""