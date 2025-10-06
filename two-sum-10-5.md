class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # function takes nums which is a list of ints and target which is and int, and outputs a list of ints 
        prevMap = {} #hashmap stores value and index

        for i, n in enumerate(nums): # looks at each number in nums, enumerate means give both both the index and the number
            diff = target - n  # find the difference to reach target 
            if diff in prevMap: 
                return [prevMap[diff], i] # if found a match 
            prevMap[n] = i 
        return 

"""
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
"""
