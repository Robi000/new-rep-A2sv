class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        leng = len(nums)
        for i in range (leng):
            for j in range(leng -1):
                if nums[j] > nums[j+ 1]:
                    nums[j+1], nums[j] = nums[j] , nums[j+1]
        return 
