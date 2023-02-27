class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        lis = [0] * len (nums)
        for x in range(2 , len(nums)):
            if nums[x] - nums[x-1] == nums[x-1] - nums[x-2]:
                lis[x] = 1+ lis[x-1]
        return sum(lis)