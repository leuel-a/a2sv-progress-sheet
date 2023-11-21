class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1): # Don't need to process the last element
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest
                
        return jumps
