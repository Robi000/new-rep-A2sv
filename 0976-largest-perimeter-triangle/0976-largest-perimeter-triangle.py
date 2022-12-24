from itertools import combinations 
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        count = 0
        nums.sort(reverse = True)
        while count + 2 < len(nums):
            check1 = nums[count] < nums[count+1] + nums[count+2]
            check2 = nums[count + 1] < nums[count] + nums[count+2]
            check3 = nums[count + 2] < nums[count+1] + nums[count]
            if check1 and check2 and check3:
                return nums[count + 2] + nums[count+1] + nums[count]
            count += 1
            
        return 0
        