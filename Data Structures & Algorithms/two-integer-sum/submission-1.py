class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i,j in enumerate(nums):
            needed = target - j
            if needed in seen:
                return [seen[needed], i]
            seen[j] = i
