class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1 for _ in range(len(nums))]

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)