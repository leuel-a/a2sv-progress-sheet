class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], idx]
            hashmap[num] = idx
        return [-1, -1]